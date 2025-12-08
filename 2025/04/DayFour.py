"""
--- Day 4: Printing Department ---
You ride the escalator down to the printing department. They're clearly getting ready for Christmas;
they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).
Decorating here will be easy: they can make their own decorations. What you really need
is a way to get further into the North Pole base while the elevators are offline.
"Actually, maybe we can help with that," one of the Elves replies when you ask for help.
"We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall,
you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."
If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.
The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram
(your puzzle input) indicating where everything is located.

For example:

..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions.
If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.
In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):

..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.

Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?

Your puzzle answer was 1493.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---

Now, the Elves just need help accessing as much of the paper as they can.
Once a roll of paper can be accessed by a forklift, it can be removed.
Once a roll of paper is removed, the forklifts might be able to access more rolls of paper,
which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?
Starting with the same example as above, here is one way you could remove as many rolls of paper as possible,
using highlighted @ to indicate that a roll of paper is about to be removed, and using x to indicate that a roll of paper was just removed:

Initial state:
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.

Remove 13 rolls of paper:
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.

Remove 12 rolls of paper:
.......x..
.@@.x.x.@x
x@@@@...@@
x.@@@@..x.
.@.@@@@.x.
.x@@@@@@.x
.x.@.@.@@@
..@@@.@@@@
.x@@@@@@@.
....@@@...

Remove 7 rolls of paper:
..........
.x@.....x.
.@@@@...xx
..@@@@....
.x.@@@@...
..@@@@@@..
...@.@.@@x
..@@@.@@@@
..x@@@@@@.
....@@@...

Remove 5 rolls of paper:
..........
..x.......
.x@@@.....
..@@@@....
...@@@@...
..x@@@@@..
...@.@.@@.
..x@@.@@@x
...@@@@@@.
....@@@...

Remove 2 rolls of paper:
..........
..........
..x@@.....
..@@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@x.
....@@@...

Remove 1 roll of paper:
..........
..........
...@@.....
..x@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
...x@.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
....x.....
...@@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Remove 1 roll of paper:
..........
..........
..........
...x@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...

Stop once no more rolls of paper are accessible by a forklift. In this example, a total of 43 rolls of paper can be removed.
Start with your original diagram. How many rolls of paper in total can be removed by the Elves and their forklifts?

Your puzzle answer was 9194.
"""

import numpy as np


def inputDocument(document: str) -> list[str]:
    with open(document, "r") as file:
        input = [line.strip() for line in file.readlines() if line.strip()]
    return input


def formateDocument(document: list[str]) -> np.ndarray:
    temp_list = [list(line) for line in document]
    return np.array(temp_list, dtype='U1')


def testCase(test: int = 0):
    if test == 0:
        return ["..@@.@@@@.",
                "@@@.@.@.@@",
                "@@@@@.@.@@",
                "@.@@@@..@.",
                "@@.@@@@.@@",
                ".@@@@@@@.@",
                ".@.@.@.@@@",
                "@.@@@.@@@@",
                ".@@@@@@@@.",
                "@.@.@@@.@."]
    else:
        return inputDocument("2025/04/input.txt")


def part1(diagram: np.ndarray) -> int:
    rows, cols = diagram.shape
    access_rolls = 0

    for y in range(rows):
        for x in range(cols):
            if diagram[y,x] == "@":
                if can_access(diagram, y, x, rows, cols):
                    access_rolls += 1
    return access_rolls


def can_access(diagram: np.ndarray, y: int, x: int, rows: int, cols: int) -> bool:
    near_by_rolls = 0
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]
    for dy, dx in directions:
        ny, nx = y + dy, x + dx

        if 0 <= ny < rows and 0 <= nx < cols:
            if diagram[ny, nx] == '@':
                near_by_rolls += 1

    return near_by_rolls < 4


def part2(diagram: np.ndarray) -> int:
    rows, cols = diagram.shape
    access_rolls = []
    remove_rolls = 0
    while True:
        for y in range(rows):
            for x in range(cols):
                if diagram[y,x] == "@":
                    if can_access(diagram, y, x, rows, cols):
                        access_rolls.append((y,x))
                        remove_rolls += 1
        if access_rolls == []:
            break
        for roll in access_rolls:
            diagram[roll[0]][roll[1]] = "."
        access_rolls = []

    return remove_rolls


if __name__ == "__main__":
    document = testCase(1)
    formatedDocment = formateDocument(document)
    print(f"Part 1: {part1(formatedDocment)}")
    print(f"Part 2: {part2(formatedDocment)}")
