"""
--- Day 9: All in a Single Night ---
Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?

Your puzzle answer was 207.

--- Part Two ---
The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?

Your puzzle answer was 804.
"""

import itertools


def inputDocument(document: str) -> list[str]:
    with open(document, "r") as file:
        input = [line.strip() for line in file.readlines() if line.strip()]
    return input


def testCase(test: int = 0):
    if test == 0:
        return ["London to Dublin = 464",
                "London to Belfast = 518",
                "Dublin to Belfast = 141"]
    else:
        return inputDocument("2015/09/input.txt")


def formatingDocument(document: list[str]) -> list[str]:
    cityToCityDintence = []
    for line in document:
        line = line.split(" ")
        cityToCityDintence.append((line[0], line[2], int(line[4])))
    return cityToCityDintence


def allCitys(formating: list[tuple[str,str,int]]) -> list[str]:
    citys = set()
    for city1, city2, _ in formating:
        citys.add(city1)
        citys.add(city2)
    return sorted(list(citys))


def calculateAllRods(cityToCityDintence: list[tuple[str,str,int]], citys:list[str]) -> list[list[str],int]:
    shortesRod = set()
    longestRod = set()
    shortestDistance = float("inf")
    longestDistance = 0
    for perm in itertools.permutations(citys):
        distance = 0
        for i in range(len(perm) - 1):
            city1, city2 = perm[i], perm[i + 1]
            for start, end, distanceBetweenCitys in formating:
                if (city1 == start and city2 == end) or (city1 == end and city2 == start):
                    distance += distanceBetweenCitys
        if distance < shortestDistance:
            shortestDistance = distance
            shortesRod = perm
        if distance > longestDistance:
            longestDistance = distance
            longestRod = perm
    return shortesRod, shortestDistance, longestRod, longestDistance


if __name__ == "__main__":
    document = testCase(1)
    formating = formatingDocument(document)
    citys = allCitys(formating)
    shortesRod, shortestDistance, longestRod, longestDistance = calculateAllRods(formating, citys)
    print(f"Part 1: {shortesRod, shortestDistance}")
    print(f"Part 2: {longestRod, longestDistance}")
