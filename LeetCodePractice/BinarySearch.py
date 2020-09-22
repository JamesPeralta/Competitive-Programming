def binary_search(arr, elem):
    left = 0
    right = len(arr) - 1

    calculations = 0
    while left <= right:
        calculations += 1
        mid = (left + right) // 2
        if elem == arr[mid]:
            print(calculations)
            return True
        elif elem < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    print(calculations)
    return False


arr = [1, 2, 4, 6, 7, 11, 22, 32, 43, 54, 54, 66, 88, 99, 442]
print(binary_search(arr, 22))
