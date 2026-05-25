class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [0] * (amount + 1)
        dp[0] = 1

        for val in range(len(coins) - 1, - 1, -1):
            for a in range(1, amount + 1):
                if coins[val] > a:
                    dp[a] += 0
                    continue
                dp[a] += dp[a - coins[val]]

        return dp[amount]