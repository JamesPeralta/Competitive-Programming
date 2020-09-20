array = [-99, 4, 2, 1, -3, 4, 92, 11, -321, 66, 1, 0]
expected = sorted(array)


def insertion_sort(array):
    for i in range(1, len(array)):
        j = i
        while j - 1 >= 0 and array[j] < array[j - 1]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1

    return array


print(expected == insertion_sort(array))
