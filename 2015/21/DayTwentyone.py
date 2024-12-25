"""
--- Day 21: RPG Simulator 20XX ---
Little Henry Case got a new video game for Christmas. It's an RPG, and he's stuck on a boss. He needs to know what equipment to buy at the shop.

He hands you the controller.

In this game, the player (you) and the enemy (the boss) take turns attacking.

The player always goes first. Each attack reduces the opponent's hit points by at least 1. The first character at or below 0 hit points loses.

Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score.

An attacker always does at least 1 damage. So, if the attacker has a damage score of 8, and the defender has an armor score of 3, the defender loses 5 hit points.

If the defender had an armor score of 300, the defender would still lose 1 hit point.

Your damage score and armor score both start at zero. They can be increased by buying items in exchange for gold.

You start with no items and have as much gold as you need. Your total damage or armor is equal to the sum of those stats from all of your items.

You have 100 hit points.

Here is what the item shop is selling:

Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
You must buy exactly one weapon; no dual-wielding. Armor is optional, but you can't use more than one. You can buy 0-2 rings (at most one for each hand).

You must use any items you buy. The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.

For example, suppose you have 8 hit points, 5 damage, and 5 armor, and that the boss has 12 hit points, 7 damage, and 2 armor:

The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.
In this scenario, the player wins! (Barely.)

You have 100 hit points. The boss's actual stats are in your puzzle input. What is the least amount of gold you can spend and still win the fight?

Your puzzle answer was 111.

--- Part Two ---
Turns out the shopkeeper is working with the boss, and can persuade you to buy whatever items he wants. The other rules still apply, and he still only has one of each item.

What is the most amount of gold you can spend and still lose the fight?

Your puzzle answer was 188.
"""

import itertools
import copy

def inputDocument(document: str) -> list[str]:
    with open(document, "r") as file:
        return [line.strip() for line in file.readlines() if line.strip()]


def testCase(test: int = 0):
    if test == 0:
        return ["Hit Points: 12",
                "Damage: 7",
                "Armor: 2"]
    else:
        return inputDocument("2015/21/input.txt")


def formatedDocument(document: list[str]) -> dict[dict[int]]:
    boss_stats = {}

    for line in document:
        key, value = line.split(": ")
        if key == "Hit Points":
            boss_stats["hitPoints"] = int(value)
        elif key == "Damage":
            boss_stats["damage"] = int(value)
        elif key == "Armor":
            boss_stats["armor"] = int(value)

    player_stats = {
        "hitPoints": 12 if boss_stats["hitPoints"] == 12 else 100,
        "damage": 5 if boss_stats["hitPoints"] == 12 else 0,
        "armor": 5 if boss_stats["hitPoints"] == 12 else 0
    }

    return {"player": player_stats, "boss": boss_stats}


def fight(game: dict[dict]) -> bool:
    player, boss = game["player"], game["boss"]

    while player["hitPoints"] > 0 and boss["hitPoints"] > 0:
        boss["hitPoints"] -= max(1, player["damage"] - boss["armor"])
        if boss["hitPoints"] <= 0:
            return True

        player["hitPoints"] -= max(1, boss["damage"] - player["armor"])
    return False


def shop():
    weapons = [(8,4,0), (10,5,0), (25,6,0), (40,7,0), (74,8,0)]
    armor = [(13,0,1), (31,0,2), (53,0,3), (75,0,4), (102,0,5)]
    rings = [(25,1,0), (50,2,0), (100,3,0), (20,0,1), (40,0,2), (80,0,3)]
    return weapons, armor, rings


def calcualteCosts(game: dict[dict]):
    weapons, armor, rings = shop()
    lowCost = float('inf')
    hightCost = 0
    for weapon in weapons:
        for r in range(3):
            for ringCombo in itertools.combinations(rings, r):
                for i in range(len(armor)):
                    state = copy.deepcopy(game)
                    if i < len(armor) // 2:
                        state["player"]["armor"] += armor[i][2]
                        cost = weapon[0] + armor[i][0] + sum(ring[0] for ring in ringCombo)
                    else:
                        cost = weapon[0] + sum(ring[0] for ring in ringCombo)

                    # Apply equipment
                    state["player"]["damage"] += sum(ring[1] for ring in ringCombo) + weapon[1]
                    state["player"]["armor"] += sum(ring[2] for ring in ringCombo)

                     # Update costs based on fight result
                    if fight(state):
                        lowCost = min(lowCost, cost)
                    else:
                        hightCost = max(hightCost, cost)
    return lowCost, hightCost




if __name__ == "__main__":
    document = testCase(1)
    game = formatedDocument(document)
    lowCost, hightsCost = calcualteCosts(game)
    print(f"Part 1: {lowCost}")
    print(f"Part 2: {hightsCost}")
