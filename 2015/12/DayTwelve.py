"""
--- Day 12: JSAbacusFramework.io ---

Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

For example:

    [1,2,3] and {"a":2,"b":4} both have a sum of 6.
    [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
    {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
    [] and {} both have a sum of 0.

You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?

Your puzzle answer was 191164.

--- Part Two ---

Uh oh - the Accounting-Elves have realized that they double-counted everything red.

Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects ({...}), not arrays ([...]).

    [1,2,3] still has a sum of 6.
    [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
    {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
    [1,"red",5] has a sum of 6, because "red" in an array has no effect.

Your puzzle answer was 87842.
"""

import json


def inputDocument(document: str) -> json.dumps:
    with open(document, "r") as file:
        input = json.load(file)
    return input


def testCase(test: int = 0):
    if test == 0:
        return json.dumps([[1,2,3],{"a":2,"b":4}])
    else:
        return inputDocument("2015/12/input.json")

def helper(obj):
    if isinstance(obj, dict):
        return sum(helper(v) for v in obj.values())
    elif isinstance(obj, list):
        return sum(helper(v) for v in obj)
    elif isinstance(obj, int):
        return obj
    else:
        return 0

def sumNumbers(document: json.dumps) -> int:
    return helper(document)


def sumNumbersWithoutRed(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(sumNumbersWithoutRed(item) for item in data)
    elif isinstance(data, dict):
        if "red" in data.values():
            return 0
        return sum(sumNumbersWithoutRed(value) for value in data.values())
    else:
        return 0


if __name__ == "__main__":
    document = testCase(1)
    print(f"Part 1: {sumNumbers(document)}")
    print(f"Part 2: {sumNumbersWithoutRed(document)}")
