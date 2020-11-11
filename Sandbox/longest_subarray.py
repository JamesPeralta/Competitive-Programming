"""
Need to know the max element

"""


def solution(A):
    
    # Numbers are limited from -10 to 10
    occurrences = [0 for i in range(20)]
    left, right, max_occur, max_length = 0, 0, 0, 0
    while right < len(A):
        occurrences[A[right] + 10] += 1
        max_occur = max(max_occur, occurrences[A[right] + 10])
        right += 1

        while max_occur + 3 < right - left:
            occurrences[A[left] + 10] -= 1
            left += 1

        max_length = max(max_length, right - left)

    return max_length

# A = [-9, 8]
# A = [1, 1, -10, 3, -10, 3, -10]
# A = [2, 3, 3, 3, 3, 1]
# A = [3, 3, 2, 1, 2, 2, 9, 3, 3]
result = solution(A)
print(result)