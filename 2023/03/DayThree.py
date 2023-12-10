"""
--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?

--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
"""

def inputDocument(document: str):
    with open(document, "r") as file:
        engineSchematic = [line.strip() for line in file.readlines() if line.strip()]
    return engineSchematic


def extraktNumber(engineSchematic: list):
    numberInSchematic = []
    symbols = ["*", "#", "+", "-", "$", "@","=","/", "&"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    length = len(engineSchematic[0])
    for engineNumber in range(len(engineSchematic)):
        number = ""
        firstPosition = 0
        lastPosition = 0
        for symbol in range(length):
            if engineSchematic[engineNumber][symbol] in numbers:
                if number == "":
                    firstPosition = symbol
                number += engineSchematic[engineNumber][symbol]
                if symbol == length-1 and engineSchematic[engineNumber][symbol] in numbers and number != "":
                    lastPosition = symbol
                    numberInSchematic.append([engineNumber, number, firstPosition, lastPosition])
            elif engineSchematic[engineNumber][symbol] == "." or engineSchematic[engineNumber][symbol] in symbols:
                if number != "":
                    lastPosition = symbol-1
                    numberInSchematic.append([engineNumber, number, firstPosition, lastPosition])
                number = ""
    return numberInSchematic


def isPartNumbers(engineSchematic: list, numbersToBeVerified: list):
    sume = 0
    symbols = ["*", "#", "+", "-", "$", "@","=","/", "&", "%"]
    lengthRow = len(engineSchematic)
    lengthColume = len(engineSchematic[0])
    for number in numbersToBeVerified:
        isValidetet = False
        i = number[0]
        for j in range(number[2],number[3]+1):
            if i+1 < lengthRow:
                if engineSchematic[i+1][j] in symbols:
                    isValidetet = True
                    break
            if i-1 >= 0:
                if engineSchematic[i-1][j] in symbols:
                    isValidetet = True
                    break
            if j-1 <= lengthColume:
                if engineSchematic[i][j-1] in symbols:
                    isValidetet = True
                    break
            if i+1 < lengthRow and j-1 > 0:
                if engineSchematic[i+1][j-1] in symbols:
                    isValidetet = True
                    break
            if i-1 >= 0 and j-1 >= 0:
                if engineSchematic[i-1][j-1] in symbols:
                    isValidetet = True
                    break
            if j+1 < lengthColume:
                if engineSchematic[i][j+1] in symbols:
                    isValidetet = True
                    break
            if i-1 >= 0 and j+1 < lengthColume:
                if engineSchematic[i-1][j+1] in symbols:
                    isValidetet = True
                    break
            if i+1 < lengthRow and j+1 < lengthColume:
                if engineSchematic[i+1][j+1] in symbols:
                    isValidetet = True
                    break
        if isValidetet:
            sume += int(number[1])
    return sume


def gearsTatio(engineSchematic: list, numbersToBeVerified: list):
    sume = 0
    symbols = ["*"]
    lengthRow = len(engineSchematic)
    lengthColume = len(engineSchematic[0])
    for number in numbersToBeVerified:
        isValidetet = False
        star = 0
        i = number[0]
        for j in range(number[2],number[3]+1):
            if i+1 < lengthRow:
                if engineSchematic[i+1][j] in symbols:
                    isValidetet = True
                    break
            if i-1 >= 0:
                if engineSchematic[i-1][j] in symbols:
                    isValidetet = True
                    break
            if j-1 <= lengthColume:
                if engineSchematic[i][j-1] in symbols:
                    isValidetet = True
                    break
            if i+1 < lengthRow and j-1 > 0:
                if engineSchematic[i+1][j-1] in symbols:
                    isValidetet = True
                    break
            if i-1 >= 0 and j-1 >= 0:
                if engineSchematic[i-1][j-1] in symbols:
                    isValidetet = True
                    break
            if j+1 < lengthColume:
                if engineSchematic[i][j+1] in symbols:
                    isValidetet = True
                    break
            if i-1 >= 0 and j+1 < lengthColume:
                if engineSchematic[i-1][j+1] in symbols:
                    isValidetet = True
                    break
            if i+1 < lengthRow and j+1 < lengthColume:
                if engineSchematic[i+1][j+1] in symbols:
                    isValidetet = True
                    break
        if isValidetet:
            for gear in numbersToBeVerified:
                if gear is not number:
                    if star >= gear[2] and star <= gear[3]:
                        sume += int(number[1]) * int(gear[1])
                        break
                    elif star-1 <= gear[3] and star > gear[2]:
                        sume += int(number[1]) * int(gear[1])
                        break
    return sume


def testCase(part: int = 0):
    if part == 0:
        return ["467..114..",
                "...*......",
                "..35..633.",
                "......#...",
                "617*......",
                ".....+.58.",
                "..592.....",
                "......755.",
                "...$.*....",
                ".664.598.."]
    elif part == 1:
        return ["12.......*..",
                "+.........34",
                ".......-12..",
                "..78........",
                "..*....60...",
                "78.........9",
                ".5.....23..$",
                "8...90*12...",
                "............",
                "2.2....12...",
                ".*.......*..",
                "1.1..503+.56"]
    else:
        return inputDocument("2023/03/DayThree.txt")


if __name__ == "__main__":
    engineSchematic = testCase(3)
    numbersToBeVerified = extraktNumber(engineSchematic)

    print("Part 1: " + str(isPartNumbers(engineSchematic,numbersToBeVerified)))
    print("Part 2: " + str(gearsTatio(engineSchematic,numbersToBeVerified)))