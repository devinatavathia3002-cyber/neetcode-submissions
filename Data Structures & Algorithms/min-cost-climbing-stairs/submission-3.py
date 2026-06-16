class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # def recurse(i):
        #     if i >= len(cost):
        #         return 0
            
        #     return min(cost[i] + recurse(i + 1), cost[i] + recurse(i + 2))
        
        # return min(recurse(0), recurse(1))

        # dp solution
        dp = [0] * (len(cost) + 1)
        dp[len(cost)] = 0
        dp[len(cost) - 1] = cost[len(cost) - 1]

        for i in range(len(cost) - 2, -1, -1):
            one = cost[i] + dp[i + 1]
            two = cost[i] + dp[i + 2]
            dp[i] = min(one, two)

        return min(dp[0], dp[1])

        # dp solution
        # dp = [0] * len(cost)
        # dp[0], dp[1] = cost[0], cost[1]

        # for i in range(2, len(cost)):
        #     dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        # return min(dp[-1], dp[-2]) 