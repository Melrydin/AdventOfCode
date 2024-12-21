"""
--- Day 16: Aunt Sue ---
Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card. However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift.

You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those compounds there are.

According to the instructions, these are what the MFCSAM can detect:

children, by human DNA age analysis.
cats. It doesn't differentiate individual breeds.
Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
goldfish. No other kinds of fish.
trees, all in one group.
cars, presumably by exhaust or gasoline or something.
perfumes, which is handy, since many of your Aunts Sue wear a few kinds.

In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM.

It beeps inquisitively at you a few times and then prints out a message on ticker tape:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1

You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.

What is the number of the Sue that got you the gift?

Your puzzle answer was 373.

--- Part Two ---
As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye. Apparently, it has an outdated retroencabulator,

and so the output from the machine isn't exact values - some of them indicate ranges.

In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen),

while the pomeranians and goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).

What is the number of the real Aunt Sue?

Your puzzle answer was 260.
"""


def inputDocument(document: str) -> list[str]:
    with open(document, "r") as file:
        input = [line.strip() for line in file.readlines() if line.strip()]
    return input


def testCase(test: int = 0):
    if test == 0:
        return []
    else:
        return inputDocument("2015/16/input.txt")


def formatedDocument(document: list[str]) -> list[dict[int]]:
    sues = []
    for sue in document:
        newSue = {}
        sue = sue.split(" ")
        newSue[sue[2][:-1]] = int(sue[3].split(",")[0])
        newSue[sue[4][:-1]] = int(sue[5].split(",")[0])
        newSue[sue[6][:-1]] = int(sue[7].split(",")[0])
        sues.append(newSue)
    return sues


def findSue(sues: list[dict[int]], keys: list[str], check: dict[int]) -> int:
    matchScore = 0
    sueNumber = 0
    for i, sue in enumerate(sues):
        matches = sum(1 for key in keys if sue.get(key) == check.get(key))
        if matchScore <= matches:
            matchScore = matches
            sueNumber = i+1
    return sueNumber


def findTheRealSue(sues, check, equal_function):
    for sue in range(len(sues)):
        if equal_function(sues[sue], check):
            return sue + 1
    return None


def equalReal(sue, check):
    for key in sue:
        if key in ["cats", "trees"]:
            if sue[key] <= check[key]:
                return False
        elif key in ["pomeranians", "goldfish"]:
            if sue[key] >= check[key]:
                return False
        elif check[key] != sue[key]:
            return False
    return True


if __name__ == "__main__":
    document = testCase(1)
    keys = ["children", "cats", "samoyeds", "pomeranians", "akitas", "vizslas", "goldfish", "trees", "cars", "perfumes"]
    check = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}
    sues = formatedDocument(document)
    print(f"Part 1: {findSue(sues, keys, check)}")
    print(f"Part 2: {findTheRealSue(sues, check,equalReal)}")
