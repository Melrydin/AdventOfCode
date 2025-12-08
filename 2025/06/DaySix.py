"""
--- Day 6: Trash Compactor ---
After helping the Elves in the kitchen, you were taking a break and helping
them re-enact a movie scene when you over-enthusiastically jumped into the garbage chute!
A brief fall later, you find yourself in a garbage smasher. Unfortunately,
the door's been magnetically sealed.
As you try to find a way out, you are approached by a family of cephalopods!
They're pretty sure they can get the door open, but it will take some time.
While you wait, they're curious if you can help the youngest cephalopod with her math homework.
Cephalopod math doesn't look that different from normal math.
The math worksheet (your puzzle input) consists of a list of problems;
each problem has a group of numbers that need to be either added (+) or multiplied (*) together.

However, the problems are arranged a little strangely;
they seem to be presented next to each other in a very long horizontal list. For example:

123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +

Each problem's numbers are arranged vertically;
at the bottom of the problem is the symbol for the operation that needs to be performed.
Problems are separated by a full column of only spaces. The left/right alignment of numbers within each problem can be ignored.
So, this worksheet contains four problems:

123 * 45 * 6 = 33210
328 + 64 + 98 = 490
51 * 387 * 215 = 4243455
64 + 23 + 314 = 401

To check their work, cephalopod students are given the grand total of adding together
all of the answers to the individual problems. In this worksheet, the grand total is 33210 + 490 + 4243455 + 401 = 4277556.
Of course, the actual worksheet is much wider.
You'll need to make sure to unroll it completely so that you can read the problems clearly.
Solve the problems on the math worksheet.
What is the grand total found by adding together all of the answers to the individual problems?

Your puzzle answer was 4387670995909.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

The big cephalopods come back to check on how things are going. When they see that your grand total doesn't
match the one expected by the worksheet, they realize they forgot to explain how to read cephalopod math.
Cephalopod math is written right-to-left in columns. Each number is given in its own column,
with the most significant digit at the top and the least significant digit at the bottom.
(Problems are still separated with a column consisting only of spaces, and the symbol at the bottom of the problem is still the operator to use.)

Here's the example worksheet again:

123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +

Reading the problems right-to-left one column at a time, the problems are now quite different:

The rightmost problem is 4 + 431 + 623 = 1058
The second problem from the right is 175 * 581 * 32 = 3253600
The third problem from the right is 8 + 248 + 369 = 625
Finally, the leftmost problem is 356 * 24 * 1 = 8544
Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.

Solve the problems on the math worksheet again.
What is the grand total found by adding together all of the answers to the individual problems?
"""

import numpy as np

def inputDocument(document: str) -> list[str]:
    with open(document, "r") as file:
        input = [line.strip() for line in file.readlines() if line.strip()]
    return input


def formateDocument(document: list[str]) -> np.ndarray:
    temp = [list(filter(None,line.split(" "))) for line in document]
    return np.array(temp, dtype='U')


def testCase(test: int = 0):
    if test == 0:
        return ["123 328  51 64 ",
                " 45 64  387 23 ",
                "  6 98  215 314",
                "*   +   *   +  " ]
    else:
        return inputDocument("2025/06/input.txt")


def part1(worksheet: list[list]) -> int:
    rows, cols = worksheet.shape
    problems_sum = 0
    for i in range(cols):
        row = worksheet[:, i]
        problems_sum += calculate(row)
    return problems_sum


def calculate(row: np.ndarray) -> int:
    symbol = row[-1]
    sum = 0
    for number in row[:-1]:
        if sum == 0:
            sum = int(number)
        elif symbol == "*":
            sum *= int(number)
        else:
            sum += int(number)
    return sum

def calculate2(row: list) -> int:
    symbol = row[-1]
    sum = numbers[0]
    numbers = row[:-1]

    if operator == '+':
        sum = sum(numbers)
    elif operator == '*':
        sum = 1
        for n in numbers:
            sum *= n


def part2(document: list[str]) -> int:
    max_len = max(len(line) for line in document)
    lines_padded = [line.ljust(max_len) for line in document]
    worksheet = np.array([list(line) for line in lines_padded])

    rows, cols = worksheet.shape
    numbers = []
    tmp = []
    operator = ""
    problems_sum = 0

    for col_idx in range(cols - 1, -1, -1):
        spalte = worksheet[:, col_idx]
        operator_char = spalte[-1]

        if operator_char != " ":
            operator = operator_char

        ziffern = [char for char in spalte[:-1] if char.isdigit()]

        if ziffern:
            zahl_string = "".join(ziffern)
            zahl = int(zahl_string)
            tmp.append(zahl)
        else:
            if tmp:
                tmp.append(operator)
                numbers.append(tmp)
                tmp = []

    if tmp:
        tmp.append(operator)
        numbers.append(tmp)

    for row in numbers:
        problems_sum += calculate(row)
    return problems_sum


if __name__ == "__main__":
    document = testCase(1)
    formatedDocment = formateDocument(document)
    print(f"Part 1: {part1(formatedDocment)}")
    print(f"Part 2: {part2(document)}")
