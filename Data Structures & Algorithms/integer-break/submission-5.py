class Solution:
    def integerBreak(self, n: int) -> int:
        
        # recursive solution

        # def recurse(target):
        #     if target == 0:
        #         return 1
        #     if target < 0:
        #         return 0

        #     res = 1
        #     for i in range(2, target + 1):
        #         remaining = target - i
        #         res = max(res, recurse(remaining) * i)
        #     return res
        
        # return recurse(n)

        # bottom-up dp
        
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = (i if i != n else 1)
            for j in range(2, n):
                dp[i] = max(dp[i], dp[j] * dp[i - j])

        return dp[n]
        