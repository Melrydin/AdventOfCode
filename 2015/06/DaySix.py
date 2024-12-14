"""
--- Day 6: Probably a Fire Hazard ---
Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?

Your puzzle answer was 377891.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.

Your puzzle answer was 14110788.
"""

import numpy as np


def inputDocument(document: str) -> list[str]:
    with open(document, "r") as file:
        input = [line.strip() for line in file.readlines() if line.strip()]
    return input


def testCase(test: int = 0):
    if test == 0:
        return []
    else:
        return inputDocument("2015/06/input.txt")


def formatDokument(document: list[str]) -> list[tuple[int,tuple[int],tuple[int]]]:
    lightInstructions = []
    for instructions in document:
        instructions = instructions.split(" ")
        start = tuple(map(int,instructions[-3].split(",")))
        end = tuple(map(int, instructions[-1].split(",")))
        if instructions[1] == "on":
            action = True
        elif instructions[1] == "off":
            action = False
        else: # toggle
            action = 3
        lightInstructions.append((action, start, end))
    return lightInstructions


def countLitLights(instructions: list[tuple[int,tuple[int],tuple[int]]]) -> int:
    lights = np.zeros(shape=(1000,1000), dtype=bool)
    for instruction in instructions:
        action, start, end = instruction
        x1, y1 = start
        x2, y2 = end
        # toggle
        if action == 3:
            lights[x1:x2+1, y1:y2+1] ^= True
        # on or off
        else:
            lights[x1:x2+1, y1:y2+1] = action
    return np.count_nonzero(lights)


def brightnessLights(instructions: list[tuple[int,tuple[int],tuple[int]]]) -> int:
    lights = np.zeros(shape=(1000,1000), dtype=np.int8)
    for instruction in instructions:
        action, start, end = instruction
        x1, y1 = start
        x2, y2 = end
        # on
        if action == 1:
            lights[x1:x2+1, y1:y2+1] += 1
        # off
        elif action == 0:
            lights[x1:x2+1, y1:y2+1] = np.maximum(lights[x1:x2+1, y1:y2+1] - 1, 0)
        else: # toggle
            lights[x1:x2+1, y1:y2+1] += 2
    return np.sum(lights)


if __name__ == "__main__":
    document = testCase(1)
    formated = formatDokument(document)
    print(f"Part 1: {countLitLights(formated)}")
    print(f"Part 2: {brightnessLights(formated)}")
