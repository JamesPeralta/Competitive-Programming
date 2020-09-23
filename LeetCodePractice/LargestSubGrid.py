def retrieve_sum(memoized, row, col, square_size):
    # Top right corner
    sum = 0
    for row in memoized[row: row + square_size]:
        left_side = row[col - square_size] if col - square_size >= 0 else 0
        right_side = row[col]
        sum += (right_side - left_side)

    return sum


def largest_sub_grid(grid, sum):
    memoized_arr = []
    # Memoize arr
    for row in grid:
        for col in range(len(row)):
            row[col] = row[col - 1] + row[col] if col - 1 >= 0 else 0 + row[col]
        memoized_arr.append(row)

    largest_k = [i for i in range(1, len(grid))]

    left = 0
    right = len(largest_k) - 1

    optimal_result = 0
    while left <= right:
        mid = (left + right) // 2
        largest_sum = None
        for row in range(0, len(grid)):
            if (row - 1) + largest_k[mid] >= len(grid):
                break
            for col in range(len(grid[0]) - 1, -1, -1):
                if (col + 1) - largest_k[mid] < 0:
                    break

                sub_arr_sum = retrieve_sum(memoized_arr, row, col, largest_k[mid])
                if largest_sum is None:
                    largest_sum = sub_arr_sum
                else:
                    largest_sum = sub_arr_sum if sub_arr_sum > largest_sum else largest_sum

        # Meets condition check above
        if largest_sum <= sum:
            optimal_result = largest_k[mid]
            left = mid + 1
        # Doesn't meet condition, check below
        else:
            right = mid - 1

    return optimal_result


# grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# grid = [[4, 5], [6, 7]]
grid = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
max_sum = 39
print(largest_sub_grid(grid, max_sum))
