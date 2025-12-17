"""
--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways and
office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department;
the walls are covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... 5 10 25?
Some of these aren't triangles. You can't help but mark the impossible ones.
In a valid triangle, the sum of any two sides must be larger than the remaining side.
For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?

Your puzzle answer was 983.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

Now that you've helpfully marked up their design documents, it occurs to you that triangles are
specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.
For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603

In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?

Your puzzle answer was 1836.
Both parts of this puzzle are complete! They provide two gold stars: **
"""


def inputDocument(document: str) -> list[str]:
    with open(document, "r") as file:
        input = [line.strip() for line in file.readlines() if line.strip()]
    return input


def formateDocument(document: list[str]):
    return [(int(line.split()[0]), int(line.split()[1]), int(line.split()[2])) for line in document]


def testCase(test: int = 0):
    if test == 0:
        return ["5 10 25"]
    else:
        return inputDocument("2016/03/input.txt")


def part1(triangles: list[tuple]) -> int:
    possible_count = 0
    for triangle in triangles:
        a, b, c = sorted(triangle)
        if (a + b > c):
            possible_count += 1
    return possible_count


def part2(triangles: list[tuple]) -> int:
    possible_count = 0
    for i in range(0, len(triangles), 3):
        row1 = triangles[i]
        row2 = triangles[i+1]
        row3 = triangles[i+2]

        t1 = [row1[0], row2[0], row3[0]]
        t2 = [row1[1], row2[1], row3[1]]
        t3 = [row1[2], row2[2], row3[2]]
        for t in [t1, t2, t3]:
            sides = sorted(t)
            if sides[0] + sides[1] > sides[2]:
                possible_count += 1

    return possible_count


if __name__ == "__main__":
    document = testCase(1)
    formatedDocment = formateDocument(document)
    print(f"Part 1: {part1(formatedDocment)}")
    print(f"Part 2: {part2(formatedDocment)}")
