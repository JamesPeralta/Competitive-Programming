# Build merge sort
# Takes in an array and returns it sorted
# How does it work, it recursively splits an array into two halves until each array is sorted
# Then it performs "merge two sorted arrays"

"""
Merge sort algo:
    1. Find middle and break into two arrays (recursively)
    2. When left and right come back join them and return this array
"""


class MergeSort:
    def sort_arr(self, arr):
        if len(arr) <= 1:
            return arr

        midpoint = len(arr) // 2
        left = self.sort_arr(arr[:midpoint])
        right = self.sort_arr(arr[midpoint:])
        left_pointer = 0
        right_pointer = 0
        arr_pointer = 0
        while left_pointer < len(left) and right_pointer < len(right):
            if left[left_pointer] < right[right_pointer]:
                arr[arr_pointer] = left[left_pointer]
                arr_pointer += 1
                left_pointer += 1
            else:
                arr[arr_pointer] = right[right_pointer]
                arr_pointer += 1
                right_pointer += 1

        while left_pointer < len(left):
            arr[arr_pointer] = left[left_pointer]
            arr_pointer += 1
            left_pointer += 1

        while right_pointer < len(right):
            arr[arr_pointer] = right[right_pointer]
            arr_pointer += 1
            right_pointer += 1

        return arr


def __main__():
    merge_sort = MergeSort()
    print(merge_sort.sort_arr([6, 11, 3]))
    print(merge_sort.sort_arr([6, 11, 1, 3, 2]))
    print(merge_sort.sort_arr([432, 11, -43, -123, 333, 564, 222, 9323423423]))


__main__()