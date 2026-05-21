class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = [[0, 0] for i in range(len(prices) + 1)]

        for i in range(len(prices) - 1, -1, -1):

            # sell
            sell = dp[i + 2][1] + prices[i] if i + 1 < len(prices) else prices[i]
            cooldown = dp[i + 1][0]
            dp[i][0] = max(cooldown, sell)

            # buy
            buy = dp[i + 1][0] - prices[i] if i + 1 < len(prices) else -prices[i]
            cooldown = dp[i + 1][1]
            dp[i][1] = max(cooldown, buy)
        
        return dp[0][1]