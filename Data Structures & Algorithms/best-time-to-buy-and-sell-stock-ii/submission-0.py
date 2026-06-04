class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for i in range(1, len(prices)):
            curr = prices[i]
            if curr > prices[i - 1]:
                res += curr - prices[i - 1]  

        return res