class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        dp = [float('inf')] * (len(days) + 1)
        # base case
        dp[len(days)] = 0

        #dayIndex = len(days) - 1
        dpIndex = len(days) - 1
        while dpIndex >= 0:
            for duration, cost in zip([1, 7, 30], costs):
                dayIndex = dpIndex
                newDay = days[dayIndex] + duration
                while dayIndex < len(days) and days[dayIndex] < newDay:
                    dayIndex += 1
                if dayIndex < len(days):
                    dp[dpIndex] = min(dp[dpIndex], cost + dp[dayIndex])
                else:
                    dp[dpIndex] = min(dp[dpIndex], cost)
            dpIndex -= 1
            
        return dp[0]

        # [1, 4, 6, 7, 8, 20]
        # [I, I, I, I, I, 2, 0]