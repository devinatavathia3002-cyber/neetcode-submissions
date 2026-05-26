class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}

        def recurse(index):
            if index >= len(days):
                return 0
            
            if index in dp:
                return dp[index]
            
            dp[index] = float('inf')
            for i in range(len(costs)):
                val = costs[i]
                newDayIndex = index
                if i == 0:
                    newDay = days[index] + 1 - 1
                    while newDayIndex < len(days) and days[newDayIndex] <= newDay:
                        newDayIndex += 1
                if i == 1:
                    newDay = days[index] + 7 - 1
                    while newDayIndex < len(days) and days[newDayIndex] <= newDay:
                        newDayIndex += 1
                if i == 2:
                    newDay = days[index] + 30 - 1
                    while newDayIndex < len(days) and days[newDayIndex] <= newDay:
                        newDayIndex += 1
                dp[index] = min(dp[index], val + recurse(newDayIndex))
            
            return dp[index]
        
        return recurse(0)