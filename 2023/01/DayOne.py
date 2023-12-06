"""
--- Day 1: Trebuchet?! ---
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?

--- Part Two ---
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
"""

def inputDocument(document: str):
    with open(document, "r") as file:
        calibrationValues = [line.strip() for line in file.readlines() if line.strip()]
    return calibrationValues


def calibrationValueNumbers(values: list):
    calibrationValue = 0
    number = ["1","2","3","4","5","6","7","8","9"]
    for value in values:
        numberOne = ""
        numberTwo = ""
        for j in value:
            if j in number:
                numberOne = j
                break
        for j in range(1,len(value)+1):
            if value[-j] in number:
                numberTwo = value[-j]
                break
        calibrationValue += int(numberOne + numberTwo)
    return calibrationValue


def calibrationValueLatters(values: list):
    calibrationValue = 0
    number = ["1","2","3","4","5","6","7","8","9"]
    numberLatter = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for value in values:
        numberOne = ""
        numberTwo = ""
        for j in range(len(value)):
            if value[j] in number:
                numberOne = value[j]
                break
            else:
                isTrue = False
                for numbers in numberLatter:
                    if numbers in value[:j+1]:
                        isTrue = True
                        numberOne = decode(numbers,numberLatter)
                        break
                if isTrue:
                    break
        for n in range(1,len(value)+1):
            if value[-n] in number:
                numberTwo = value[-n]
                break
            else:
                isTrue = False
                for numbers in numberLatter:
                    if numbers in value[-n:]:
                        isTrue = True
                        numberTwo = decode(numbers,numberLatter)
                        break
                if isTrue:
                    break
        calibrationValue += int(numberOne + numberTwo)
    return calibrationValue
    

def decode(latters: str, numberLatter: list):
    if numberLatter[0] in latters:
        return "1"
    elif numberLatter[1] in latters:
        return "2"
    elif numberLatter[2] in latters:
        return "3"
    elif numberLatter[3] in latters:
        return "4"
    elif numberLatter[4] in latters:
        return "5"
    elif numberLatter[5] in latters:
        return "6"
    elif numberLatter[6] in latters:
        return "7"
    elif numberLatter[7] in latters:
        return "8"
    else:
        return "9"


def testCase(part: int = 0):
    if part == 0:
        return ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
    elif part == 1:
        return ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
    else:
        return inputDocument("DayOne.txt")


if __name__ == "__main__":
    calibrationValue = testCase(2)
    
    print("Part 1: {}".format(calibrationValueNumbers(calibrationValue)))
    print("Part 2: {}".format(calibrationValueLatters(calibrationValue)))