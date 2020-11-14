import string
char_map = dict(zip(range(1, 27), string.ascii_lowercase))

first_line = input().split()

length = int(first_line[0])
height = int(first_line[1])
k = int(first_line[2])

laptop_back = [["_" for j in range(length)] for i in range(height)]


def is_oob(row, col):
    if not (0 <= row < height):
        return True
    elif not (0 <= col < length):
        return True

    return False


def place_sticker(row, col, l, h, char):
    for i in range(row, row + h):
        for j in range(col, col + l):
            if is_oob(i, j):
                continue
            laptop_back[i][j] = char_map[char + 1]



for index, line in enumerate(range(k)):
    row_input = list(map(lambda x: int(x), input().split()))
    leng, hei, col, row = row_input[0], row_input[1], row_input[2], row_input[3]
    place_sticker(row, col, leng, hei, index)

for row in laptop_back:
    print("".join(row))