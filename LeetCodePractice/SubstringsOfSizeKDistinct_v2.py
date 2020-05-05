"""
Ex 1)
    Input: s = "abcabc", k = 3
    Output: ["abc", "bca", "cab"]

Ex 2)
    Input: s = "abacab", k = 3
    Output: ["bac", "cab"]

Ex 3)
    Input: s = "awaglknagawunagwkwagl", k = 4
    Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
"""

input_string = input("Input a string: ")
substring_length = int(input("Enter in the length for all unique substrings: "))


def retrieve_all_substrings():
    if len(input_string) < substring_length:
        return []

    unique_substrings_list = []  # Used to maintain the order
    unique_substrings = set()

    for start_index in range(0, (len(input_string) - substring_length) + 1):
        end_index = start_index + substring_length

        distinct_chars = set()

        subset_is_distinct = True
        candidate_substring = input_string[start_index: end_index]
        for char in candidate_substring:
            if char in distinct_chars:
                subset_is_distinct = False
                break

            distinct_chars.add(char)

        if subset_is_distinct and candidate_substring not in unique_substrings:
            unique_substrings.add(candidate_substring)
            unique_substrings_list.append(candidate_substring)

    return unique_substrings_list


print(retrieve_all_substrings())
