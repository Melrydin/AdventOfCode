"""
--- Day 4: Ceres Search ---

"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:

..X...
.SAMX.
.A..A.
XMAS.S
.X....

The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

Take a look at the little Elf's word search. How many times does XMAS appear?

Your puzzle answer was 2599.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S

Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........

In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?
"""


def inputDocument(document: str):
    with open(document, "r") as file:
        input = [line.strip() for line in file.readlines() if line.strip()]
    return input


def testCase(part: int = 0):
    if part == 0:
        return ["MMMSXXMASM",
                "MSAMXMSMSA",
                "AMXSXMAAMM",
                "MSAMASMSMX",
                "XMASAMXAMM",
                "XXAMMXXAMA",
                "SMSMSASXSS",
                "SAXAMASAAA",
                "MAMMMXMMMM",
                "MXMXAXMASX"]
    else:
        return inputDocument("2024/04/input.txt")


def wordSearcher(document: list[str]) -> int:
    word = "XMAS"
    grid = document
    count = 0
    count += wordSearchInLine(grid, word)
    count += wordSearchOverLines(grid, word)
    return count


def wordSearchInLine(grid: list[str], word: str) -> int:
    count = 0
    for row in grid:
        # Search the lines horizontally
        for i in range(len(row) - len(word) + 1):
            testWord = row[i:i + len(word)]
            if testWord == word or testWord[::-1] == word:
                count += 1
    return count


def wordSearchOverLines(grid: list[str], word: str) -> int:
    count = 0
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)

    # Search vertically
    for row in range(rows - word_len + 1):
        for col in range(cols):
            testWord = "".join(grid[row + i][col] for i in range(word_len))
            if testWord == word or testWord[::-1] == word:
                count += 1

    # Search diagonally (top left to bottom right)
    for row in range(rows - word_len + 1):
        for col in range(cols - word_len + 1):
            testWord = "".join(grid[row + i][col + i] for i in range(word_len))
            if testWord == word or testWord[::-1] == word:
                count += 1

    # Search diagonally (top right to bottom left)
    for row in range(rows - word_len + 1):
        for col in range(word_len - 1, cols):
            testWord = "".join(grid[row + i][col - i] for i in range(word_len))
            if testWord == word or testWord[::-1] == word:
                count += 1

    return count


def xMasX(grid: list[list[str]], word) -> int:
    count = 0
    for row in range(len(grid)-2):
        for col in range(len(grid[row]) - 2):
            verticalWordLelft = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
            verticalWordRight = grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]
            if (verticalWordLelft == word or verticalWordLelft[::-1] == word) and (verticalWordRight == word or verticalWordRight[::-1] == word):
                count += 1
    return count


if __name__ == "__main__":
    document = testCase(1)
    print(f"Part 1: {wordSearcher(document)}")
    print(f"Part 2: {xMasX(document, "MAS")}")