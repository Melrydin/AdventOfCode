"""
--- Day 13: Knights of the Dinner Table ---
In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year, you resolve, will be different.

You're going to find the optimal seating arrangement and avoid all those awkward conversations.

You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person.

You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.

For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:

Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much), but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.

If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41).

The arrangement looks like this:

     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83
After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.

What is the total change in happiness for the optimal seating arrangement of the actual guest list?

Your puzzle answer was 618.

--- Part Two ---
In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to.

You assume everyone else would be just as ambivalent about sitting next to you, too.

So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

What is the total change in happiness for the optimal seating arrangement that actually includes yourself?

Your puzzle answer was 601.
"""

import itertools


def inputDocument(document: str) -> list[str]:
    with open(document, "r") as file:
        input = [line.strip() for line in file.readlines() if line.strip()]
    return input


def testCase(test: int = 0):
    if test == 0:
        return ["Alice would gain 54 happiness units by sitting next to Bob.",
                "Alice would lose 79 happiness units by sitting next to Carol.",
                "Alice would lose 2 happiness units by sitting next to David.",
                "Bob would gain 83 happiness units by sitting next to Alice.",
                "Bob would lose 7 happiness units by sitting next to Carol.",
                "Bob would lose 63 happiness units by sitting next to David.",
                "Carol would lose 62 happiness units by sitting next to Alice.",
                "Carol would gain 60 happiness units by sitting next to Bob.",
                "Carol would gain 55 happiness units by sitting next to David.",
                "David would gain 46 happiness units by sitting next to Alice.",
                "David would lose 7 happiness units by sitting next to Bob.",
                "David would gain 41 happiness units by sitting next to Carol."]
    else:
        return inputDocument("2015/13/input.txt")


def formatDocument(document: list[str]) -> list[tuple[str,int,str]]:
    seatingArrangements = []
    for sitting in document:
        sitting = sitting.split(" ")
        person1, gainOrLoss, happiness, person2 = sitting[0], sitting[2], int(sitting[3]), sitting[10].strip(".")
        if gainOrLoss == "lose":
            happiness *= -1
        seatingArrangements.append((person1,int(happiness), person2))
    return seatingArrangements


def findAllMembers(orders: list[tuple[str,int,str]]) -> list[str]:
    members = set()
    for order in orders:
        members.add(order[0])
        members.add(order[2])
    return list(members)


def findOptimalSeatingArrangement(orders: list[tuple[str, int, str]], members: list[str]) -> int:
    seatingArrangements = itertools.permutations(members)
    happiness = 0
    for seatingArrangement in seatingArrangements:
        currentHappiness = calculateHappiness(seatingArrangement,orders)
        if happiness < currentHappiness:
            happiness = currentHappiness
    return happiness


def calculateHappiness(seatingArrangements: list[str], orders: list[tuple[str, int, str]]) -> int:
    happiness = 0
    for seating in range(len(seatingArrangements)):
        if seating == 0:
            left = seatingArrangements[len(seatingArrangements)-1]
            right = seatingArrangements[seating+1]
        elif seating == len(seatingArrangements)-1:
            left = seatingArrangements[seating-1]
            right = seatingArrangements[0]
        else:
            left = seatingArrangements[seating-1]
            right = seatingArrangements[seating+1]
        middle = seatingArrangements[seating]
        for order in orders:
            if order[0] == middle and (order[2] == left or order[2] == right):
                happiness += order[1]
    return happiness


if __name__ == "__main__":
    document = testCase(1)
    formattedDoc = formatDocument(document)
    members = findAllMembers(formattedDoc)
    print(f"Part 1: {findOptimalSeatingArrangement(formattedDoc,members)}")
    members.append("MySelf")
    print(f"Part 2: {findOptimalSeatingArrangement(formattedDoc,members)}")
