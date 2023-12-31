"""
--- Day 11: Cosmic Expansion ---

You continue following signs for "Hot Springs" and eventually come across an observatory. The Elf within turns out to be a researcher studying cosmic expansion using the giant telescope here.

He doesn't know anything about the missing machine parts; he's only visiting for this research project. However, he confirms that the hot springs are the next-closest area likely to have people; he'll even take you straight there once he's done with today's observation analysis.

Maybe you can help him with the analysis to speed things up?

The researcher has collected a bunch of data and compiled the data into a single giant image (your puzzle input). The image includes empty space (.) and galaxies (#). For example:

...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....

The researcher is trying to figure out the sum of the lengths of the shortest path between every pair of galaxies. However, there's a catch: the universe expanded in the time it took the light from those galaxies to reach the observatory.

Due to something involving gravitational effects, only some space expands. In fact, the result is that any rows or columns that contain no galaxies should all actually be twice as big.

In the above example, three columns and two rows contain no galaxies:

   v  v  v
 ...#......
 .......#..
 #.........
>..........<
 ......#...
 .#........
 .........#
>..........<
 .......#..
 #...#.....
   ^  ^  ^

These rows and columns need to be twice as big; the result of cosmic expansion therefore looks like this:

....#........
.........#...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#.......

Equipped with this expanded universe, the shortest path between every pair of galaxies can be found. It can help to assign every galaxy a unique number:

....1........
.........2...
3............
.............
.............
........4....
.5...........
............6
.............
.............
.........7...
8....9.......

In these 9 galaxies, there are 36 pairs. Only count each pair once; order within the pair doesn't matter. For each pair, find any shortest path between the two galaxies using only steps that move up, down, left, or right exactly one . or # at a time. (The shortest path between two galaxies is allowed to pass through another galaxy.)

For example, here is one of the shortest paths between galaxies 5 and 9:

....1........
.........2...
3............
.............
.............
........4....
.5...........
.##.........6
..##.........
...##........
....##...7...
8....9.......

This path has length 9 because it takes a minimum of nine steps to get from galaxy 5 to galaxy 9 (the eight locations marked # plus the step onto galaxy 9 itself). Here are some other example shortest path lengths:

    Between galaxy 1 and galaxy 7: 15
    Between galaxy 3 and galaxy 6: 17
    Between galaxy 8 and galaxy 9: 5

In this example, after expanding the universe, the sum of the shortest path between all 36 pairs of galaxies is 374.

Expand the universe, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?
--- Part Two ---

The galaxies are much older (and thus much farther apart) than the researcher initially estimated.

Now, instead of the expansion you did before, make each empty row or column one million times larger. That is, each empty row should be replaced with 1000000 empty rows, and each empty column should be replaced with 1000000 empty columns.

(In the example above, if each empty row or column were merely 10 times larger, the sum of the shortest paths between every pair of galaxies would be 1030. If each empty row or column were merely 100 times larger, the sum of the shortest paths between every pair of galaxies would be 8410. However, your universe will need to expand far beyond these values.)

Starting with the same initial image, expand the universe according to these new rules, then find the length of the shortest path between every pair of galaxies. What is the sum of these lengths?
"""

import numpy as np
import time

def inputDocument(document: str):
    with open(document, "r") as file:
        input = [line.strip() for line in file.readlines() if line.strip()]
    return input


def formating(input: list):
    galaxyCounter = 1
    lenInput = len(input)

    galaxyMap = np.zeros((lenInput,lenInput), dtype=int)
    galaxyPosion = [(zeile, spalte) for zeile, zeichen in enumerate(input) for spalte, symbol in enumerate(zeichen) if symbol == '#']

    for galaxy in galaxyPosion:
        galaxyMap[galaxy[0]][galaxy[1]] = galaxyCounter
        galaxyCounter += 1
    return galaxyMap


def expandeUniverse(input: np.array, expansion: int):
    lenInput = len(input)
    emptyRows = [row for row in range(lenInput) if sum(input[row]) == 0]
    emptyColumns = [column for column in range(lenInput) if sum(input[:,column]) == 0]

    counter = 0
    for i in emptyRows:
        for ex in range(0,expansion-1):
            input = np.insert(input, i + ex + counter, np.zeros(len(input[0])), axis=0)
        counter += expansion -1

    counter = 0
    for i in emptyColumns:
        for ex in range(0,expansion-1):
            input = np.insert(input, i + ex + counter, np.zeros(len(input[:,0])), axis=1)
        counter += expansion -1
    return input
    

def galaxiesPairSume(input_array: np.array):
    sumDistance = 0
    checked = set()

    nonZeroIndices = np.nonzero(input_array)
    nonZeroCoordinates = list(zip(nonZeroIndices[0], nonZeroIndices[1]))

    for i, j in nonZeroCoordinates:
        if input_array[i][j] not in checked:
            checked.add(input_array[i][j])

            distances = np.abs(i - nonZeroIndices[0]) + np.abs(j - nonZeroIndices[1])
            sumDistance += np.sum(distances)
            
    sumDistance /= 2

    return int(sumDistance)
                            

def testCase(part: int = 0):
    if part == 0:
        return ["...#......",
                ".......#..",
                "#.........",
                "..........",
                "......#...",
                ".#........",
                ".........#",
                "..........",
                ".......#..",
                "#...#....."]
    else:
        return inputDocument("2023/11/DayEleven.txt")



if __name__ == "__main__":
    input = testCase(1)
    format = formating(input)
    expant = expandeUniverse(format,2)
    startTime = time.time()
    print("Part 1: {}".format(galaxiesPairSume(expant)))
    expant = expandeUniverse(format,100)
    print("Part 2: {}".format(galaxiesPairSume(expant)))