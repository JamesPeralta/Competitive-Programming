# Implement binary search
"""
What is it searching for? Ints, Strings, Objects?
What do you want me to return if its not in the list?
    - Null, -1, exception?

Should we assume the input is sorted? or do we sort it and then perform binary search? But that would take longer
than the search

Design
Search for: 4.5
 0  1  2  3  4  5   6
[1, 3, 4, 5, 6, 7, 23]
       ^  ^

# Finding midpoint
midpoint = (right + left) // 2

Three cases

midpoint = elem
    return
midpoint < elem
    look at the right (move left to midpoint + 1)
midpoint > elem
    look at the left (move right to midpoint -1)
"""


class BinarySearch:
    @staticmethod
    def find_element(arr, to_find):
        left = 0
        right = len(arr) - 1
        while left <= right:
            midpoint = (left + right) // 2
            if arr[midpoint] == to_find:
                return midpoint
            elif arr[midpoint] < to_find:
                left = midpoint + 1
            else:
                right = midpoint - 1

        return -1


def __main__():
    b_search = BinarySearch()
    #      0  1  2  3  4  5  6
    arr = [1, 3, 4, 5, 6, 7, 23]
    print(b_search.find_element(arr, 23))  # Return: 6
    print(b_search.find_element(arr, 3))  # Return: 1
    print(b_search.find_element(arr, 33))  # Return: -1
    print(b_search.find_element(arr, 4))  # Return: 2
    print(b_search.find_element(arr, 5))  # Return: 3
    print(b_search.find_element(arr, 1.5))  # Return: -1


__main__()
