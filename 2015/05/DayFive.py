"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

For example:

    ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
    aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
    jchzalrnumimnmhp is naughty because it has no double letter.
    haegwjzuvuyypxyu is naughty because it contains the string xy.
    dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?

Your puzzle answer was 258.

--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice.

None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa),
    but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

For example:

    qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
    xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
    uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
    ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

How many strings are nice under these new rules?

Your puzzle answer was 53.
"""


def inputDocument(document: str) -> list[str]:
    with open(document, "r") as file:
        input = [line.strip() for line in file.readlines() if line.strip()]
    return input


def testCase(test: int = 0):
    if test == 0:
        return ["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]
    elif test == 1:
        return ["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy"]
    else:
        return inputDocument("2015/05/input.txt")


def niceWord(word: str) -> bool:
    vowels = "aeiou"
    counter = 0
    doubles = False
    notInSubword = ["ab", "cd", "pq", "xy"]
    for symbol in word:
        if symbol in vowels:
            counter += 1
        elif counter >= 3:
            break
    if counter < 3:
        return False
    doubles = any(word[i] == word[i+1] for i in range(len(word) - 1))
    if doubles == False:
        return False
    for i in notInSubword:
        if i in word:
            return False
    if doubles:
        return True
    return False


def niceWordNewRules(word: str) -> bool:
    doubles = any(word[i] == word[i+2] for i in range(len(word) - 2))
    hasPair = False
    for i in range(len(word) - 1):
        wordCopy = word.replace(word[i:i+2], "")
        if len(word) - 4 == len(wordCopy):
            hasPair = True
            break
    return hasPair and doubles


def wordChecker(words: list[str]) -> int:
    niceCountPartOne = 0
    niceCountPartTwo = 0
    for word in words:
        if niceWord(word):
            niceCountPartOne += 1
        if niceWordNewRules(word):
            niceCountPartTwo += 1
    return niceCountPartOne, niceCountPartTwo


if __name__ == "__main__":
    document = testCase(2)
    niceCountPartOne, niceCountPartTwo = wordChecker(document)
    print(f"Part 1: {niceCountPartOne}")
    print(f"Part 2: {niceCountPartTwo}")
