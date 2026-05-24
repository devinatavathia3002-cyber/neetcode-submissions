class Solution:
    def numSquares(self, n: int) -> int:
        # with cache
        # dp = {} # dp cache
    
        # def recurse(total):
        #     if total == n:
        #         return 0
        #     if total > n:
        #         return float("inf")
        #     if total in dp:
        #         return dp[total]
            
        #     res = n
        #     for i in range(1, int(n ** 0.5) + 1):
        #         new = i * i
        #         res = min(res, recurse(total + new) + 1)
        #     dp[total] = res
        #     return res
        
        # return recurse(0)

        # with dp

        dp = [n] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                new = j * j
                if new > i:
                    break
                else:
                    dp[i] = min(dp[i], 1 + dp[i - new])
        
        return dp[n]

            