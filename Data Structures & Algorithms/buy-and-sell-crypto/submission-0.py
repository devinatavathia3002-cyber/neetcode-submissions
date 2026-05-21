class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minimum = prices[0]
        difference = 0

        for num in prices:
            if num < minimum:
                minimum = num
            else:
                if (num - minimum) > difference:
                    difference = (num - minimum)
        
        return difference

