"""
--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
"""

import hashlib


def inputDocument(document: str) -> str:
    with open(document, "r") as file:
        return next(line.strip() for line in file if line.strip())


def testCase(test: int = 0):
    if test == 0:
        return "abcdef"
    elif test == 1:
        return "pqrstuv"
    else:
        return inputDocument("2015/04/input.txt")


def foundHash(document: str, zeros: str = "00000") -> int:
    n = 1
    while True:
        key = document + str(n)
        hashResult = hashlib.md5(key.encode()).hexdigest()
        if hashResult.startswith(zeros):
            return n, hashResult
        n += 1


if __name__ == "__main__":
    document = testCase(2)
    n, hashResult = foundHash(document)
    n2, hashResult2 = foundHash(document, "000000")
    print(f"Part 1: {n} Mit Hash: {hashResult}")
    print(f"Part 2: {n2} Mit Hash: {hashResult2}")
