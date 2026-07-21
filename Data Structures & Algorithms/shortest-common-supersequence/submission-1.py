class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j

        for r in range(1, n + 1):
            for c in range(1, m + 1):
                curr1, curr2 = str1[r - 1], str2[c - 1]
                if curr1 == curr2:
                    dp[r][c] = 1 + dp[r - 1][c - 1]
                else:
                    dp[r][c] = min(
                        1 + dp[r-1][c],
                        1 + dp[r][c - 1]
                    )
        
        # traceback
        res = []
        i, j = n, m

        while i > 0 and j > 0:
            currI, currJ = str1[i - 1], str2[j - 1]
            if currI == currJ:
                res.append(currI)
                i -= 1
                j -= 1
            else:
                if dp[i - 1][j] < dp[i][j - 1]:
                    res.append(currI)
                    i -= 1
                else:
                    res.append(currJ)
                    j -= 1
        
        while i > 0:
            res.append(str1[i - 1])
            i -= 1
        while j > 0:
            res.append(str2[j - 1])
            j -= 1

        return "".join(reversed(res))
