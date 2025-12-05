"""
--- Day 1: No Time for a Taxicab ---

Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars.

Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar;

the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get -
#
# the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North.

Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination.

Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

For example:

    Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
    R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
    R5, L5, R5, R3 leaves you 12 blocks away.

How many blocks away is Easter Bunny HQ?

Your puzzle answer was 246.

--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?

Your puzzle answer was 124.
"""


def inputDocument(document: str) -> list[str]:
    with open(document, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]


def testCase(test: int = 0):
    if test == 0:
        return ["R2, L3"]
    elif test == 1:
        return ["R2, R2, R2"]
    elif test == 2:
        return ["R5, L5, R5, R3"]
    else:
        return inputDocument("2016/01/input.txt")


def formatedDocument(document: list[str]) -> list[str]:
    instactions = []
    for line in document:
        line = line.split(", ")
        for i in line:
            direction, distance = i[0], int(i[1:])
            instactions.append((direction, distance))
    return instactions


def navigate(instructions: list[str]) -> tuple[int, int]:
    alignment = 0  # 0: North, 1: East, 2: South, 3: West
    x, y = 0, 0
    visited = set()
    first_visited_twice = None

    visited.add((x, y))  # Startposition markieren

    for direction, distance in instructions:
        # Update the direction
        if direction == "R":
            alignment = (alignment + 1) % 4
        else:  # direction == "L"
            alignment = (alignment - 1) % 4

        # Move step by step in the current direction
        for _ in range(distance):
            if alignment == 0:  # North
                y += 1
            elif alignment == 1:  # East
                x += 1
            elif alignment == 2:  # South
                y -= 1
            elif alignment == 3:  # West
                x -= 1

            # Check if this position was visited before
            if (x, y) in visited and first_visited_twice is None:
                first_visited_twice = abs(x) + abs(y)
            visited.add((x, y))

    # Calculate Manhattan distance from the final position
    manhattan_distance = abs(x) + abs(y)

    return manhattan_distance, first_visited_twice


if __name__ == "__main__":
    document = testCase(3)
    instactions = formatedDocument(document)
    manhattanDistance, visitedTwice = navigate(instactions)
    print(f"Part 1: {manhattanDistance}")
    print(f"Part 2: {visitedTwice}")
