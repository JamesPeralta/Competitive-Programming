from collections import deque
figures = {
    1: [(0, 0)],
    2: [(0, 0), (0, 1), (0, 2)],
    3: [(0, 0), (0, 1), (1, 0), (1, 1)],
    4: [(0, 0), (1, 0), (2, 0), (1, 1)],
    5: [(0, 1), (1, 0), (1, 1), (1, 2)]
}


def is_oob_or_taken(array, row, col):
    if row < 0 or row >= len(array):
        return True

    if col < 0 or col >= len(array[0]):
        return True

    if array[row][col] != 0:
        return True

    return False


def place_figure(array, row, col, figure, tag, clear=False):
    slots = figures[figure]

    # Clear a cell (b/c we're doing it all inplace)
    if clear:
        for slot in slots:
            array[row + slot[0]][col + slot[1]] = 0

        return True

    for slot in slots:
        if is_oob_or_taken(array, row + slot[0], col + slot[1]):
            return False

    for slot in slots:
        array[row + slot[0]][col + slot[1]] = tag

    return True


def __main__(n, m, figures):
    figures = deque(figures)
    array = [[0 for j in range(m)] for i in range(n)]

    for row in range(n):
        for col in range(m):
            # Try placing
            if place_figure(array, row, col, figures[0], 1) is False:
                continue
            to_place = figures.popleft()

            # recurse/ back track if necessary
            if back_track(array, figures, 2) is False:
                # Reverse my placement
                place_figure(array, row, col, to_place, 1, clear=True)
                figures.appendleft(to_place)

            if len(figures) <= 0:
                return array


def back_track(array, figures, tag):
    if len(figures) <= 0:
        return True

    for row in range(len(array)):
        for col in range(len(array[0])):
            if place_figure(array, row, col, figures[0], tag) is False:
                continue

            # Consume figure
            to_place = figures.popleft()
            # recurse/ back track if necessary
            if back_track(array, figures, tag + 1) is False:
                # Reverse my placement
                place_figure(array, row, col, to_place, tag + 1, clear=True)
                figures.appendleft(to_place)

            if len(figures) <= 0:
                return True

    return False


print(__main__(4, 4, [4, 2, 1, 3]))
