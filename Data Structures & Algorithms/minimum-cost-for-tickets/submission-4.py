class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (len(days) + 1)

        for i in range(len(days) - 1, -1, -1):
            
            # skip one day
            nextIndex = i
            newCovered = days[i] + 1 - 1
            while nextIndex < len(days) and days[nextIndex] <= newCovered:
                nextIndex += 1
            skipOne = dp[nextIndex] + costs[0]
    
            # skip seven days
            nextIndex = i
            newCovered = days[i] + 7 - 1
            while nextIndex < len(days) and days[nextIndex] <= newCovered:
                nextIndex += 1
            skipSeven = dp[nextIndex] + costs[1]
                
            # skip 30 days
            nextIndex = i
            newCovered = days[i] + 30 - 1
            while nextIndex < len(days) and days[nextIndex] <= newCovered:
                nextIndex += 1
            skipThirty = dp[nextIndex] + costs[2]

            dp[i] = min(skipOne, skipSeven, skipThirty)
        
        return dp[0]