class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False
        
        grid = [[False for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
        grid[len(s2)][len(s1)] = True

        for i in range(len(s2), -1, -1):
             for j in range(len(s1), -1, -1):
                if i < len(s2) and s3[i + j] == s2[i] and grid[i + 1][j] == True:
                    grid[i][j] = True
                if j < len(s1) and s3[i + j] == s1[j] and grid[i][j + 1] == True:
                    grid[i][j] = True
        
        return grid[0][0]
