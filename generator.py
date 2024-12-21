import argparse
import os
from datetime import datetime

def create_structure(year, day):
    dayDict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
               11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
               18: "Eighteen", 19: "Nineteen", 20: "Twenty", 21: "Twentyone", 22: "Twentytwo", 23: "Twentythree", 24: "Twentyfour", 25: "Twentyfive"}

    # Create paths
    path = os.path.join(str(year), f"{str(day).zfill(2)}")
    if os.path.exists(path):
        print(f"Folder {path} already exists. No changes made.")
        return

    os.makedirs(path, exist_ok=True)

    # Create files
    input_file = os.path.join(path, "input.txt")
    script_file = os.path.join(path, f"Day{dayDict.get(day, f'{day:03d}')}.py")

    # Create input.txt
    with open(input_file, 'w') as f:
        f.write("")  # Empty file

    # Create DayX.py
    with open(script_file, 'w') as f:
        f.write(
                f'"""\n'
                f'\n'
                f'"""\n'
                f'\n'
                f'\n'
                f'def inputDocument(document: str) -> list[str]:\n'
                f'    with open(document, "r") as file:\n'
                f'        input = [line.strip() for line in file.readlines() if line.strip()]\n'
                f'    return input\n'
                f'\n'
                f'\n'
                f'def testCase(test: int = 0):\n'
                f'    if test == 0:\n'
                f'        return []\n'
                f'    else:\n'
                f'        return inputDocument("{year}/{str(day).zfill(2)}/input.txt")\n'
                f'\n'
                f'\n'
                f'if __name__ == "__main__":\n'
                f'    document = testCase(0)\n'
                )

    print(f"Folder and files created in: {path}")

if __name__ == "__main__":
    # Define arguments
    parser = argparse.ArgumentParser(description="Creates a folder structure for a year and a day.")
    parser.add_argument('-y','--year', type=int, help="Year (e.g., 2024 or 24)")
    parser.add_argument('-d','--day', type=int, help="Day (e.g., 1, 2, ... 25)")

    # Parse arguments
    args = parser.parse_args()

    # Use current year and current day if not specified
    now = datetime.now()
    year = args.year if args.year else now.year
    if year < 100:  # If year is entered as a two-digit number
        year += 2000
    day = args.day if args.day else now.timetuple().tm_yday

    # Create structure
    create_structure(year, day)
