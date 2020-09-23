def min_cost(arr):
    for house in range(1, len(arr)):
        for material in range(0, 3):
            # best choice for material 0
            if material == 0:
                arr[house][material] = arr[house][material] + min([arr[house - 1][1], arr[house - 1][2]])
            # best choice for material 1
            elif material == 1:
                arr[house][material] = arr[house][material] + min([arr[house - 1][0], arr[house - 1][2]])
            # best choice for material 2
            else:
                arr[house][material] = arr[house][material] + min([arr[house - 1][0], arr[house - 1][1]])

    return min(arr[-1])


# arr = [[1, 2, 2], [2, 3, 3], [3, 3, 1]]
# arr = [[1, 2, 2], [2, 2, 1], [2, 1, 2]]
arr = [[0, 2, 3]]
print(min_cost(arr))
