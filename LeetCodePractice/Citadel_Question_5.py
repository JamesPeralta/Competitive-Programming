class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 0
        i = 1

        while self.calculate_series(i) <= N:
            if (N - self.calculate_series(i)) % i == 0:
                count += 1

            i += 1

        return count

    def calculate_series(self, i):
        """
        Calculates series from 1 + 2 + .. + i
        """
        return (i * (i + 1)) / 2