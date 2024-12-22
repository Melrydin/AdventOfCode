import numpy as np



def liveOrDead(playground: np.array, row: int, column: int, width: int, height: int):
    if deadByLoneliness(playground, row, column, width, height):
        return 0
    elif deadByOverpopulation(playground, row, column, width, height):
        return 0
    elif born(playground, row, column, width, height):
        return 1
    elif live(playground, row, column, width, height):
        return 1
    else:
        return 0


def born(playground: np.array, row: int, column: int, width: int, height: int):
    if playground[row][column] == 0 and countNeighbours(playground, row, column, width, height) == 3:
        return True
    else:
        return False


def live(playground: np.array, row: int, column: int, width: int, height: int):
    if playground[row][column] == 1 and countNeighbours(playground, row, column, width, height) == 2 or countNeighbours(playground, row, column, width, height) == 3:
        return True
    else:
        return False


def deadByLoneliness(playground: np.array, row: int, column: int, width: int, height: int):
    if countNeighbours(playground, row, column, width, height) < 2:
        return True
    else:
        return False


def deadByOverpopulation(playground: np.array, row: int, column: int, width: int, height: int):
    if countNeighbours(playground, row, column, width, height) > 3:
        return True
    else:
        return False


def countNeighbours(playground: np.array, row: int, column: int, width: int, height: int):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0) and 0 <= row + i < height and 0 <= column + j < width:
                if playground[row + i, column + j] == 1:
                    count += 1
    return count
