"""
Link here: https://leetcode.com/discuss/interview-question/731453/Citadel-SWE-Intern-OA-(Summer-2021)
"""
# Algo
before = [[1, 2],
          [3, 6]]

after = [[0 for j in range(len(before[0]))] for i in range(len(before))]


def modify(before_arr, after_arr, x, y):
    s = 0
    for row in range(0, x + 1):
        for col in range(0, y + 1):
            s += before_arr[row][col]
    after_arr[x][y] = s


for i in range(len(before)):
    for j in range(len(after)):
        modify(before, after, i, j)

# Clear before
for i in range(len(before)):
    for j in range(len(before[0])):
        before[i][j] = 0


def get_value(x, y):
    if x < 0 or y < 0:
        return 0

    return after[x][y]


for row in range(0, len(after)):
    for col in range(0, len(after[0])):
        # Base cases for rows
        if row == 0:
            before[row][col] = get_value(row, col) - get_value(row, col - 1)
            continue

        # Bases cases for columns
        if col == 0:
            before[row][col] = get_value(row, col) - get_value(row - 1, col)
            continue

        # Other cases
        above_contribution = get_value(row - 1, col)
        row_contribution = get_value(row, col - 1) - get_value(row - 1, col - 1)
        before[row][col] = get_value(row, col) - above_contribution - row_contribution

print(before)