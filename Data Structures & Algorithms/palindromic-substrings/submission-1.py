class Solution:
    def countSubstrings(self, s: str) -> int:
        
        count = 0
        length = len(s)
        grid = [[False for _ in range(length)] for _ in range(length)]

        for r in range(length - 1, -1, -1):
            for c in range(r, length):
                if s[r] == s[c] and (c - r <= 2 or grid[r + 1][c - 1]):
                    count += 1
                    grid[r][c] = True

        return count