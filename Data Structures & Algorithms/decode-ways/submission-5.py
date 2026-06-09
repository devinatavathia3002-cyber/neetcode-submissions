class Solution:
    def numDecodings(self, s: str) -> int:
        
        # recursive approach
        # def findTotal(i):
        #     if i >= len(s):
        #         return 1
        #     if s[i] == "0":
        #         return 0
            
        #     if i + 1 < len(s) and int(s[i:i+2]) <= 26:
        #         return findTotal(i + 1) + findTotal(i + 2)
        #     else:
        #         return findTotal(i + 1)

        # return findTotal(0)

        # dp solution
        dp = [0] * len(s)
        dp[0] = 1 if int(s[0]) != 0 else 0
        
        for i in range(1, len(s)):
            both = int(s[i - 1: i + 1])
            single = int(s[i])

            if single != 0:
                dp[i] += dp[i-1]
            if 10 <= both <= 26:
                dp[i] += dp[i-2] if i >= 2 else 1

        return dp[len(s) - 1]