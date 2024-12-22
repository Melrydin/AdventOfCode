"""
--- Day 18: Like a GIF For Your Yard ---
After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration based on the current one.

Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals).

Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

1B5...
234...
......
..123.
..8A4.
..765.

The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
All of the lights update simultaneously; they all consider the same current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:  After 1 step:   After 2 steps:  After 3 steps:  After 4 steps:
.#.#.#          ..##..          ..###.          ...#..          ......
...##.          ..##.#          ......          ......          ......
#....#          ...##.          ..###.          ...#..          ..##..
..#...          ......          ......          ..##..          ..##..
#.#..#          #.....          .#....          ......          ......
####..          #.##..          .#....          ......          ......

After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?

Your puzzle answer was 768.

--- Part Two ---
You flip the instructions over; Santa goes on to point out that this is all just an implementation of Conway's Game of Life.

At least, it was, until you notice that something's wrong with the grid of lights you bought: four lights, one in each corner, are stuck on and can't be turned off.

The example above will actually run like this:

Initial state:  After 1 step:   After 2 steps:  After 3 steps:
##.#.#          #.##.#          #..#.#          #...##
...##.          ####.#          #....#          ####.#
#....#          ...##.          .#.##.          ..##.#
..#...          ......          ...##.          ......
#.#..#          #...#.          .#..##          ##....
####.#          #.####          ##.###          ####.#

After 4 steps:  After 5 steps:
#.####          ##.###
#....#          .##..#
...#..          .##...
.##...          .##...
#.....          #.#...
#.#..#          ##...#

After 5 steps, this example now has 17 lights on.

In your grid of 100x100 lights, given your initial configuration, but with the four corners always in the on state, how many lights are on after 100 steps?

"""

import numpy as np
from rules import liveOrDead


def inputDocument(document: str) -> list[str]:
    with open(document, "r") as file:
        input = [line.strip() for line in file.readlines() if line.strip()]
    return input


def testCase(test: int = 0):
    if test == 0:
        return [".#.#.#",
                "...##.",
                "#....#",
                "..#...",
                "#.#..#",
                "####.."]
    elif test == 1:
        return ["##.#.#",
                "...##.",
                "#....#",
                "..#...",
                "#.#..#",
                "####.#"]
    else:
        return inputDocument("2015/18/input.txt")


class Playground():


    def __init__(self, document: list[str]):
        self.document = document
        self.width = len(document)
        self.height = len(document[0])
        self.playground = np.zeros((self.width, self.height), dtype=int)


    def firstGeneration(self):
        for y, line in enumerate(self.document):
            for x, char in enumerate(line):
                self.playground[y, x] = char == "#"
        return self.playground


    def nextGeneration(self):
        nextPlayground = np.zeros([self.width, self.height], dtype=int)
        for row in range(self.width):
            for column in range(self.height):
                nextPlayground[row][column] = liveOrDead(self.playground, row, column, self.width, self.height)
        self.playground = nextPlayground


    def nextGenerationWithLightsStuckOn(self):
        self.playground[0][0] = self.playground[0][self.height - 1] = self.playground[self.width - 1][0] = self.playground[self.width - 1][self.height - 1] = 1
        self.nextGeneration()
        self.playground[0][0] = self.playground[0][self.height - 1] = self.playground[self.width - 1][0] = self.playground[self.width - 1][self.height - 1] = 1


    def printPlayground(self):
        for row in range(self.width):
            print("[" + "".join(str(number) for number in self.playground[row]) + "]")
        print("\n")


if __name__ == "__main__":
    document = testCase(2)
    playground = Playground(document)
    playground.firstGeneration()
    for _ in range(100):
        playground.nextGeneration()
    print(f"Part 1: {np.sum(playground.playground)}")
    playground = Playground(document)
    playground.firstGeneration()
    for _ in range(100):
        playground.nextGenerationWithLightsStuckOn()
    print(f"Part 2: {np.sum(playground.playground)}")
