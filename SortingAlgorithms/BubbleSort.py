array = [2, 1]
expected = sorted(array)


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - (i + 1)):
            if array[j] > array[j + 1]:
                temp_left = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp_left

    return array

print(expected == bubble_sort(array))
