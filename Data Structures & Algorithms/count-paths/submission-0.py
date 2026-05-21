class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        oldRow = [1] * (n + 1)

        while m > 1:
            newRow = [0] * (n + 1)
            for i in range(n - 1, -1, -1):
                newRow[i] = oldRow[i] + newRow[i + 1]
            oldRow = newRow
            m -= 1
        
        return oldRow[0]
