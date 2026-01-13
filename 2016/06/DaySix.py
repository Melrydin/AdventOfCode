"""
--- Day 6: Signals and Noise ---

Something is jamming your communications with Santa. Fortunately,
your signal is only partially jammed, and protocol in situations like this
is to switch to a simple repetition code to get the message through.
In this model, the same message is sent repeatedly.
You've recorded the repeating message signal (your puzzle input),
but the data seems quite corrupted - almost too badly to recover. Almost.
All you need to do is figure out which character is most frequent for each position.
For example, suppose you had recorded the following messages:

eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar

The most common character in the first column is e; in the second, a; in the third, s, and so on.
Combining these characters returns the error-corrected message, easter.
Given the recording in your puzzle input, what is the error-corrected version of the message being sent?

Your puzzle answer was afwlyyyq.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

Of course, that would be the message - if you hadn't agreed to use a modified repetition code instead.
In this modified code, the sender instead transmits what looks like random data, but for each character,
the character they actually want to send is slightly less likely than the others. Even after signal-jamming noise,
you can look at the letter distributions in each column and choose the least common letter to reconstruct the original message.
In the above example, the least common character in the first column is a; in the second, d, and so on.
Repeating this process for the remaining characters produces the original message, advent.
Given the recording in your puzzle input and this new decoding methodology, what is the original message that Santa is trying to send?

Your puzzle answer was bhkzekao.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

import numpy as np

def inputDocument(document: str) -> list[str]:
    with open(document, "r") as file:
        input = [line.strip() for line in file.readlines() if line.strip()]
    return input


def formateDocument(document: list[str]):
    temp_list = [list(line) for line in document]
    return np.array(temp_list, dtype='U1')

def testCase(test: int = 0):
    if test == 0:
        return ["eedadn",
                "drvtee",
                "eandsr",
                "raavrd",
                "atevrs",
                "tsrnev",
                "sdttsa",
                "rasrtv",
                "nssdts",
                "ntnada",
                "svetve",
                "tesnvt",
                "vntsnd",
                "vrdear",
                "dvrsen",
                "enarar"]
    else:
        return inputDocument("2016/06/input.txt")


def part1(input: np.ndarray) -> str:
    _ , colums = input.shape
    message = ""
    for i in range(colums):
        colum = input[:,i]
        char, value = np.unique(colum, return_counts=True)
        max_index = np.argmax(value)
        most_common_char = char[max_index]

        message += most_common_char
    return message




def part2(input: np.ndarray) -> int:
    _ , colums = input.shape
    message = ""
    for i in range(colums):
        colum = input[:,i]
        char, value = np.unique(colum, return_counts=True)
        min_index = np.argmin(value)
        most_common_char = char[min_index]

        message += most_common_char
    return message


if __name__ == "__main__":
    document = testCase(1)
    formatedDocment = formateDocument(document)
    print(f"Part 1: {part1(formatedDocment)}")
    print(f"Part 2: {part2(formatedDocment)}")
