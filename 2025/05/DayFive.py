"""
--- Day 5: Cafeteria ---
As the forklifts break through the wall, the Elves are delighted to discover that there was a cafeteria on the other side after all.
You can hear a commotion coming from the kitchen. "At this rate, we won't have any time left to put the wreaths up in the dining hall!" Resolute in your quest, you investigate
"If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims. You ask what's going on.
The Elves in the kitchen explain the situation: because of their complicated new inventory management system, they can't figure out which of their ingredients are fresh and which are spoiled.
When you ask how it works, they give you a copy of their database (your puzzle input).
The database operates on ingredient IDs. It consists of a list of fresh ingredient ID ranges, a blank line, and a list of available ingredient IDs. For example:

3-5
10-14
16-20
12-18

1
5
8
11
17
32

The fresh ID ranges are inclusive: the range 3-5 means that ingredient IDs 3, 4, and 5 are all fresh. The ranges can also overlap; an ingredient ID is fresh if it is in any range.
The Elves are trying to determine which of the available ingredient IDs are fresh. In this example, this is done as follows:

Ingredient ID 1 is spoiled because it does not fall into any range.
Ingredient ID 5 is fresh because it falls into range 3-5.
Ingredient ID 8 is spoiled.
Ingredient ID 11 is fresh because it falls into range 10-14.
Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
Ingredient ID 32 is spoiled.

So, in this example, 3 of the available ingredient IDs are fresh.
Process the database file from the new inventory management system. How many of the available ingredient IDs are fresh?

Your puzzle answer was 517.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

The Elves start bringing their spoiled inventory to the trash chute at the back of the kitchen.
So that they can stop bugging you when they get new inventory, the Elves would like to know all of the IDs that the fresh ingredient ID ranges consider to be fresh.
An ingredient ID is still considered fresh if it is in any range.
Now, the second section of the database (the available ingredient IDs) is irrelevant. Here are the fresh ingredient ID ranges from the above example:

3-5
10-14
16-20
12-18

The ingredient IDs that these ranges consider to be fresh are 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and 20. So, in this example,
the fresh ingredient ID ranges consider a total of 14 ingredient IDs to be fresh.
Process the database file again. How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges?

"""


def inputDocument(document: str) -> list[str]:
    with open(document, "r") as file:
        input = [line.strip() for line in file.readlines() if line.strip()]
    return input


def formateDocument(document: list[str]) -> list[list, list]:
    freshIngredientIDRanges = []
    ingredientID = []
    for line in document:
        if "-" in line:
            pair = line.split("-")
            freshIngredientIDRanges.append((int(pair[0]), int(pair[1])))
        else:
            ingredientID.append(int(line))

    return [freshIngredientIDRanges, ingredientID]


def testCase(test: int = 0):
    if test == 0:
        return ["3-5", "10-14", "16-20", "12-18",
                "1", "5", "8", "11", "17", "32"]
    else:
        return inputDocument("2025/05/input.txt")


def part1(database: list[list, list]):
    freshCount = 0
    for ingredientID in database[1]:
        is_fresh = False
        for freshIngredientIDRanges in database[0]:
            if freshIngredientIDRanges[0] <= ingredientID <= freshIngredientIDRanges[1]:
                is_fresh = True
                break
        if is_fresh:
            freshCount += 1
    return freshCount


def part2(database: list[list, list]):
    ranges = database[0]
    ranges.sort(key=lambda x: x[0])

    merged_ranges = []
    current_start, current_end = ranges[0]

    for i in range(1, len(ranges)):
        next_start, next_end = ranges[i]

        if next_start <= current_end + 1:
            current_end = max(current_end, next_end)
        else:
            merged_ranges.append((current_start, current_end))
            current_start, current_end = next_start, next_end
    merged_ranges.append((current_start, current_end))

    total_count = 0
    for start, end in merged_ranges:
        total_count += (end - start + 1)
    return total_count


if __name__ == "__main__":
    document = testCase(1)
    formatedDocment = formateDocument(document)
    print(f"Part 1: {part1(formatedDocment)}")
    print(f"Part 2: {part2(formatedDocment)}")
