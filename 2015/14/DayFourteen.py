"""
--- Day 14: Reindeer Olympics ---
This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km.

On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting.

They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point).

So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?

Your puzzle answer was 2655.

--- Part Two ---
Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple reindeer tied for the lead, they each get one point.)

He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays in the lead until several seconds into Comet's second burst:

after the 140th second, Comet pulls into the lead and gets his first point. Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?

Your puzzle answer was 1059.
"""


def inputDocument(document: str) -> list[str]:
    with open(document, "r") as file:
        input = [line.strip() for line in file.readlines() if line.strip()]
    return input


def testCase(test: int = 0):
    if test == 0:
        return ["Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
                "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."]
    else:
        return inputDocument("2015/14/input.txt")


def formatDocument(document: list[str]) -> list[tuple[str, int, int, int, int, bool, int, int, int]]:
    reindeers = []
    for reindeer in document:
        reindeer = reindeer.split(" ")
        name, flySpeed, maxFlyTime, minRestTime = reindeer[0], int(reindeer[3]), int(reindeer[6]), int(reindeer[13])
        flyTime, restTime, distance, points, rest = 0,0,0,0, False
        reindeers.append((name, flySpeed, maxFlyTime, minRestTime, flyTime, rest, restTime, distance, points))
    return reindeers


def reindeersRace(reindeers: list[tuple[str, int, int, int, int, bool, int, int, int]], raceTime: int) -> tuple[int, int]:
    for time in range(raceTime):
        # Update all reindeers for the current second
        for i in range(len(reindeers)):
            reindeers[i] = calculateReindeer(reindeers[i])

        # Determine the lead distance
        max_distance = max(reindeer[7] for reindeer in reindeers)

        # Award points to all reindeers in the lead
        for i in range(len(reindeers)):
            if reindeers[i][7] == max_distance:
                # Increment points
                reindeer = list(reindeers[i])
                reindeer[8] += 1  # Update points
                reindeers[i] = tuple(reindeer)

    # Calculate the best distance and points
    bestDistance = max(reindeer[7] for reindeer in reindeers)
    maxPoints = max(reindeer[8] for reindeer in reindeers)

    return bestDistance, maxPoints


def calculateReindeer(reindeer: tuple[str, int, int, int, int, bool, int, int, int]) -> tuple[str, int, int, int, int, bool, int, int, int]:
    name, flySpeed, maxFlyTime, minRestTime, flyTime, rest, restTime, distance, points = reindeer
    if not rest:
        # Flying
        distance += flySpeed
        flyTime += 1
        if flyTime >= maxFlyTime:
            rest = True
            flyTime = 0
    else:
        # Resting
        restTime += 1
        if restTime >= minRestTime:
            rest = False
            restTime = 0
    return (name, flySpeed, maxFlyTime, minRestTime, flyTime, rest, restTime, distance, points)



if __name__ == "__main__":
    document = testCase(1)
    reindeers = formatDocument(document)
    distance, points = reindeersRace(reindeers, 2503)
    print(f"Part 1: {distance}")
    print(f"Part 2: {points}")
