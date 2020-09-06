class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        results = []

        dp_table = [[0] * 26]
        # Perform prefix sum
        for i in range(1, len(s) + 1):
            new_row = dp_table[i - 1][:]  # Copy from last row
            new_row[ord(s[i - 1]) - ord("a")] += 1
            dp_table.append(new_row)

        for left, right, k in queries:
            is_even = len(s[left: right + 1]) % 2 == 0  # boolean stating if this is odd or not

            # Base case
            if (right + 1) - left == 1:
                results.append(True)
                continue

            occurences = [R - L for (R, L) in zip(dp_table[right + 1], dp_table[left])]
            odds = 0
            for letter in occurences:
                if letter % 2 != 0 and letter > 0:
                    odds += 1

            # Even cases
            if is_even and odds / 2 <= k:
                results.append(True)
                continue
            # Odd cases
            if is_even is False and (odds - 1) / 2 <= k:
                results.append(True)
                continue

            results.append(False)

        return results