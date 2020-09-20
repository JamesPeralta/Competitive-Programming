array = [2, 1, 321, 4, 11, -2, 42, -99]
expected = sorted(array)


def bubble_sort(array):
    for i in range(len(array)):
        for j in range(len(array) - (i + 1)):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    print(array)
    return array

print(expected == bubble_sort(array))
