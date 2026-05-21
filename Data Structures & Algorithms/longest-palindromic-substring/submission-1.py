class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        ROWS = len(s)
        COLS = len(s)
        longest = ""

        grid = [[False for _ in range(COLS)] for _ in range(ROWS)]

        for i in range (len(s) - 1, -1, -1):
            for j in range(i, COLS):
                if s[i] == s[j]:
                    if j - i >= 2:
                        if grid[i + 1][j - 1]:
                            pal = s[i: j + 1]
                            if len(pal) > len(longest):
                                longest = pal
                            grid[i][j] = True
                    else:
                        pal = s[i: j + 1]
                        if len(pal) > len(longest):
                            longest = pal
                        grid[i][j] = True
                    
        return longest

