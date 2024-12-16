"""
--- Day 11: Corporate Policy ---

Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

    Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
    Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
    Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.

For example:

    hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
    abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
    abbcegjk fails the third requirement, because it only has one double letter (bb).
    The next password after abcdefgh is abcdffaa.
    The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.

Given Santa's current password (your puzzle input), what should his next password be?

Your puzzle input is hxbxwxba.

Your puzzle answer was hxbxxyzz.

--- Part Two ---

Santa's password expired again. What's the next one?

Your puzzle answer was hxcaabcc.
"""


def testCase(test: int = 0):
    if test == 0:
        return "abcdefgh"
    else:
        return "hxbxwxba"


def isValid(password: str) -> bool:
    # hove increasing strainght of three letters
    strainght = any(ord(password[i]) + 1 == ord(password[i + 1]) and
                    ord(password[i + 1]) + 1 == ord(password[i + 2])
                    for i in range(len(password) - 2))
    if strainght == False:
        return False

    # not in password
    if any(c in password for c in "iol"):
        return False

    # check has tow pairs
    pairs = set()
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            pairs.add(password[i])
            i += 1
        i += 1
    if len(pairs) < 2:
        return False

    return True


def newPassword(password: str) -> str:
    password = list(password)
    for i in range(len(password) - 1, -1, -1):
            if password[i] == 'z':
                password[i] = 'a'
            else:
                password[i] = chr(ord(password[i]) + 1)
                break
    return ''.join(password)


def generateNewPassword(password: str) -> str:
    while not isValid(password):
        password = newPassword(password)
    return password

if __name__ == "__main__":
    document = testCase(1)
    password = generateNewPassword(document)
    print(f"Part 1: {password}")
    print(f"Part 2: {generateNewPassword(generateNewPassword(newPassword(password)))}")
