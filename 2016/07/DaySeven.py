"""
--- Day 7: Internet Protocol Version 7 ---

While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited).
You'd like to figure out which IPs support TLS (transport-layer snooping).
An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA.
An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair,
such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

For example:

    abba[mnop]qrst supports TLS (abba outside square brackets).
    abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
    aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
    ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).

How many IPs in your puzzle input support TLS?
Your puzzle answer was 105.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

You would also like to know which IPs support SSL (super-secret listening).
An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections),
and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences.
An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba.
A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.

For example:

    aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
    xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
    aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
    zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).

How many IPs in your puzzle input support SSL?

Your puzzle answer was 258.

Both parts of this puzzle are complete! They provide two gold stars: **

"""

import re


def inputDocument(document: str) -> list[str]:
    with open(document, "r") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
    return lines


def testCase(test: int = 0):
    if test == 0:
        return ["abba[mnop]qrst",
                "abcd[bddb]xyyx",
                "aaaa[qwer]tyui",
                "ioxxoj[asdfgh]zxcvbn"]
    else:
        return inputDocument("2016/07/input.txt")


def part1(lines) -> int:
    tls_counter = 0

    for ip in lines:
        parts = re.split(r'\[|\]', ip)

        supernets = parts[0::2]
        hypernets = parts[1::2]

        abba_outside = any(has_abba(s) for s in supernets)
        abba_inside = any(has_abba(s) for s in hypernets)

        if abba_outside and not abba_inside:
            tls_counter += 1

    return tls_counter

def has_abba(s: str) -> bool:
    for i in range(len(s) - 3):
        if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
            return True
    return False


def part2(lines) -> int:
    ssl_counter = 0

    for ip in lines:
        parts = re.split(r'\[|\]', ip)
        supernets = parts[0::2]
        hypernets = parts[1::2]

        abas = {aba for s in supernets for aba in get_abas(s)}

        for aba in abas:
            bab = aba[1] + aba[0] + aba[1]
            if any(bab in h for h in hypernets):
                ssl_counter += 1
                break

    return ssl_counter

def get_abas(s: str) -> list[str]:
    found_abas = []
    for i in range(len(s) - 2):
        if s[i] == s[i+2] and s[i] != s[i+1]:
            found_abas.append(s[i:i+3])
    return found_abas


if __name__ == "__main__":
    document = testCase(1)
    print(f"Part 1: {part1(document)}")
    print(f"Part 2: {part2(document)}")
