"""
--- Day 7: Bridge Repair ---

The Historians take you to a familiar rope bridge over a river in the middle of a jungle. The Chief isn't on this side of the bridge, though; maybe he's on the other side?

When you go to cross the bridge, you notice a group of engineers trying to repair it. (Apparently, it breaks pretty frequently.) You won't be able to cross until it's fixed.

You ask how long it'll take; the engineers tell you that it only needs final calibrations, but some young elephants were playing nearby and stole all the operators from their calibration equations! They could finish the calibrations if only someone could determine which test values could possibly be produced by placing any combination of operators into their calibration equations (your puzzle input).

For example:

190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20

Each line represents a single equation. The test value appears before the colon on each line; it is your job to determine whether the remaining numbers can be combined with operators to produce the test value.

Operators are always evaluated left-to-right, not according to precedence rules. Furthermore, numbers in the equations cannot be rearranged. Glancing into the jungle, you can see elephants holding two different types of operators: add (+) and multiply (*).

Only three of the above equations can be made true by inserting operators:

    190: 10 19 has only one position that accepts an operator: between 10 and 19. Choosing + would give 29, but choosing * would give the test value (10 * 19 = 190).
    3267: 81 40 27 has two positions for operators. Of the four possible configurations of the operators, two cause the right side to match the test value: 81 + 40 * 27 and 81 * 40 + 27 both equal 3267 (when evaluated left-to-right)!
    292: 11 6 16 20 can be solved in exactly one way: 11 + 6 * 16 + 20.

The engineers just need the total calibration result, which is the sum of the test values from just the equations that could possibly be true. In the above example, the sum of the test values for the three equations listed above is 3749.

Determine which equations could possibly be true. What is their total calibration result?

Your puzzle answer was 1545311493300.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

The engineers seem concerned; the total calibration result you gave them is nowhere close to being within safety tolerances. Just then, you spot your mistake: some well-hidden elephants are holding a third type of operator.

The concatenation operator (||) combines the digits from its left and right inputs into a single number. For example, 12 || 345 would become 12345. All operators are still evaluated left-to-right.

Now, apart from the three equations that could be made true using only addition and multiplication, the above example has three more equations that can be made true by inserting operators:

    156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
    7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
    192: 17 8 14 can be made true using 17 || 8 + 14.

Adding up all six test values (the three that could be made before using only + and * plus the new three that can now be made by also using ||) produces the new total calibration result of 11387.

Using your new knowledge of elephant hiding spots, determine which equations could possibly be true. What is their total calibration result?
"""

import math

def inputDocument(document: str):
    with open(document, "r") as file:
        input = [line.strip() for line in file.readlines() if line.strip()]
    return input

def testCase(part: int = 0):
    if part == 0:
        return ["190: 10 19",
                "3267: 81 40 27",
                "83: 17 5",
                "156: 15 6",
                "7290: 6 8 6 15",
                "161011: 16 10 13",
                "192: 17 8 14",
                "21037: 9 7 18 13",
                "292: 11 6 16 20"]
    else:
        return inputDocument("2024/07/input.txt")
    

def formatDocument(document: list[str]) -> list[tuple[int]]:
    return [(int(test_value), list(map(int, equation.split()))) for test_value, equation in (line.split(": ") for line in document)]


def calculate(target: int, numbers: list[int], combine: bool) -> bool:
    n = len(numbers)
    stack = [(numbers[0], 1)]
    while stack:
        currentValue, index = stack.pop()
        if index == n:
            if currentValue == target:
                return True
            continue
        # Add
        stack.append((currentValue + numbers[index], index + 1))
        # Multiply
        stack.append((currentValue * numbers[index], index + 1))
        if combine:
            # Combines
            nextNumber = numbers[index]
            combinedValue = currentValue * (10 ** (math.floor(math.log10(nextNumber)) + 1)) + nextNumber
            stack.append((combinedValue, index + 1))
    return False


def solve(document: list[tuple[int, list[int]]]) -> int:
    totalPart1 = 0
    totalPart2 = 0
    for target, numbers in document:
        if calculate(target, numbers, False):
            totalPart1 += target
        if calculate(target, numbers, True):
            totalPart2 += target
    return totalPart1, totalPart2
    

if __name__ == "__main__":
    document = testCase(1)
    format = formatDocument(document)
    p1, p2 = solve(format)
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")