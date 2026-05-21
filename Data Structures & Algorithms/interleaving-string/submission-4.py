class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # def recurse(i1, i2, i3):
        #     if i3 == len(s3):
        #         return True
        #     if i1 >= len(s1) and i2 >= len(s2):
        #         return False
            
        #     if i1 < len(s1) and s1[i1] == s3[i3] and i2 < len(s2) and s2[i2] == s3[i3]:
        #         return recurse(i1 + 1, i2, i3 + 1) or recurse(i1, i2 + 1, i3 + 1)
        #     elif i1 < len(s1) and s1[i1] == s3[i3]:
        #         return recurse(i1 + 1, i2, i3 + 1)
        #     elif i2 < len(s2) and s2[i2] == s3[i3]:
        #         return recurse(i1, i2 + 1, i3 + 1)
        #     else:
        #         return False
        
        # return recurse(0, 0, 0)

        # with dp

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


