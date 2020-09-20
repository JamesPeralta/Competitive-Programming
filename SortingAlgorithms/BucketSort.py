import random

array = [random.random() for _ in range(10)]
expected = sorted(array)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j - 1 >= 0 and arr[j] < arr[j - 1]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

    return arr


def bucket_sort(arr):
    # Create buckets
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Place in buckets
    for elem in arr:
        buckets[int(elem * n)].append(elem)

    # Perform insertion sort on each bucket
    for i in range(len(buckets)):
        buckets[i] = insertion_sort(buckets[i])

    # Stitch back all arrays
    final_arr = []
    for bucket in buckets:
        final_arr += bucket

    print(final_arr)
    return final_arr


print(expected == bucket_sort(array))