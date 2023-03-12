from typing import List, Tuple

def get_neighbours(
    array: List[List[int]], x: int, y: int, filter_none_values: bool = True, k: int = 4) -> List[int]:
    """Returns a list of 4 (k=4) or 8 (k=8) neighbours
    of the cell (x, y).

    k = 4       k = 8
    _ 0 _       0 1 2
    3 x 1       7 x 3
    _ 2 _       6 5 4

    """
    dim = len(array)
    neighbours = []
    if k == 4:
        if x - 1 < 0:
            neighbours.append(-1)
        else:
            neighbours.append(array[x - 1][y])
        if y + 1 >= dim:
            neighbours.append(-1)
        else:
            neighbours.append(array[x][y + 1])
        if x + 1 >= dim:
            neighbours.append(-1)
        else:
            neighbours.append(array[x + 1][y])
        if y - 1 < 0:
            neighbours.append(-1)
        else:
            neighbours.append(array[x][y - 1])

    else:
        # k == 8
        if x - 1 < 0 or y - 1 < 0:
            neighbours.append(-1)
        else:
            neighbours.append(array[x - 1][y - 1])

        if x - 1 < 0:
            neighbours.append(-1)
        else:
            neighbours.append(array[x - 1][y])

        if x - 1 < 0 or y + 1 >= dim:
            neighbours.append(-1)
        else:
            neighbours.append(array[x - 1][y + 1])

        if y + 1 >= dim:
            neighbours.append(-1)
        else:
            neighbours.append(array[x][y + 1])

        if x + 1 >= dim or y + 1 >= dim:
            neighbours.append(-1)
        else:
            neighbours.append(array[x + 1][y + 1])

        if x + 1 >= dim:
            neighbours.append(-1)
        else:
            neighbours.append(array[x + 1][y])

        if x + 1 >= dim or y - 1 < 0:
            neighbours.append(-1)
        else:
            neighbours.append(array[x + 1][y - 1])

        if y - 1 < 0:
            neighbours.append(-1)
        else:
            neighbours.append(array[x][y - 1])

    if filter_none_values:
        neighbours = [n for n in neighbours if n != -1]

    return neighbours