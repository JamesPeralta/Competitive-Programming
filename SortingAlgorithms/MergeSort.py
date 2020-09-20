tests = [[2],
         [6, 1, 4],
         [38, 27, 43, 3, 9, 82, 10],
         [38, 27, 43, 3, 9, 82, 10, 6, 1, 4, 38, 27, 43, 3, 9, 82]]


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    middle = len(arr) // 2
    left_half = merge_sort(arr[:middle])
    right_half = merge_sort(arr[middle:])

    left_pointer = 0
    right_pointer = 0

    merged_arr = []
    while True:
        if left_half[left_pointer] < right_half[right_pointer]:
            merged_arr.append(left_half[left_pointer])
            left_pointer += 1
        else:
            merged_arr.append(right_half[right_pointer])
            right_pointer += 1

        if left_pointer == len(left_half):
            merged_arr = merged_arr + right_half[right_pointer:]
            break

        if right_pointer == len(right_half):
            merged_arr = merged_arr + left_half[left_pointer:]
            break

    return merged_arr


def __main__():
    for i, arr in enumerate(tests):
        if sorted(arr) == merge_sort(arr):
            print("Test {} PASSED".format(i))
            print(merge_sort(arr))
        else:
            print("Test {} FAILED".format(i))
            print(merge_sort(arr))


__main__()
