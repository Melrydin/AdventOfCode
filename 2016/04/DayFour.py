"""
--- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data,
but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.
Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.
A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

    aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
    a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
    not-a-real-room-404[oarel] is a real room.
    totally-real-room-200[decoy] is not.

Of the real rooms from the list above, the sum of their sector IDs is 1514.
What is the sum of the sector IDs of the real rooms?

Your puzzle answer was 361724.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

With all the decoy data out of the way, it's time to decrypt this list and get moving.
The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software.
However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.
To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID.
A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?

Your puzzle answer was 482.

Both parts of this puzzle are complete! They provide two gold stars: **
"""

import re
from collections import Counter
from dataclasses import dataclass


def inputDocument(document: str) -> list[str]:
    with open(document, "r") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
    return lines


def formateDocument(document: list[str]):
    rooms = []
    pattern = re.compile(r"^(.*)-(\d+)\[(.*)\]$")

    for entry in document:
        match = pattern.match(entry.strip())
        if match:
            rooms.append(Room(
                name=match.group(1),
                id=int(match.group(2)),
                checksum=match.group(3)
            ))

    return rooms

@dataclass
class Room:
    name: str
    id: int
    checksum: str


def testCase(test: int = 0):
    if test == 0:
        return ["aaaaa-bbb-z-y-x-123[abxyz]",
                "a-b-c-d-e-f-g-h-987[abcde]",
                "not-a-real-room-404[oarel]",
                "totally-real-room-200[decoy]"]
    else:
        return inputDocument("2016/04/input.txt")


def part1(lines) -> tuple[int, list]:
    real_room_id_sum = 0
    real_room = []
    for room in lines:
        counts = Counter(room.name.replace("-",""))
        sorted_chars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        calculated_checksum = "".join([char for char, count in sorted_chars[:5]])
        if calculated_checksum == room.checksum:
            real_room_id_sum += room.id
            real_room.append(room)
    return (real_room_id_sum, real_room)


def part2(lines) -> int:
    for room in lines:
        decrypted_name = decrypt_name(room.name, room.id)
        if "north" in decrypted_name:
            return room.id


def decrypt_name(encrypted_name: str, sector_id: int) -> str:
    result = []
    for char in encrypted_name:
        if char == "-":
            result.append(" ")
        else:
            offset = ord(char) - ord('a')
            shifted = (offset + sector_id) % 26
            new_char = chr(shifted + ord('a'))
            result.append(new_char)
    return "".join(result)

if __name__ == "__main__":
    document = testCase(1)
    formatedDocment = formateDocument(document)
    id_sum_and_rooms = part1(formatedDocment)
    print(f"Part 1: {id_sum_and_rooms[0]}")
    print(f"Part 2: {part2(id_sum_and_rooms[1])}")
