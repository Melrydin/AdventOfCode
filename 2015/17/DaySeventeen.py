"""
--- Day 17: No Such Thing as Too Much ---
The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5
Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?

Your puzzle answer was 654.

--- Part Two ---
While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number of containers and still hold exactly 150 litres?

In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3.

"""

import itertools


def testCase(test: int = 0):
    if test == 0:
        return [20,15,10,5,5]
    else:
        return [50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40]


def countCombinations(capacities: list[int], totalVolume: int) -> int:
    combinationCounter = 0
    for r in range(1, len(capacities)+ 1):
        for combination in itertools.combinations(capacities,r):
            if sum(combination) == totalVolume:
                combinationCounter += 1
    return combinationCounter


def foundMinCombination(capacities: list[int], totalVolume: int) -> int:
    for r in range(1, len(capacities)+ 1):
        for combination in itertools.combinations(capacities,r):
            if sum(combination) == totalVolume:
                return len(combination)


def countMinCombinations(capacities: list[int], totalVolume: int, minCombination: int) -> int:
    combinationCounter = 0
    for combination in itertools.combinations(capacities,minCombination):
        if sum(combination) == totalVolume:
            combinationCounter += 1
    return combinationCounter



if __name__ == "__main__":
    capacities = testCase(1)
    print(f"Part 1: {countCombinations(capacities, 150)}")
    print(f"Part 2: {countMinCombinations(capacities, 150,foundMinCombination(capacities, 150))}")
