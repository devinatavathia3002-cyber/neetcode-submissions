class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        counter = 1
        total = 1
        while counter <= abs(n):
            total *= x
            counter += 1
        
        if n < 0:
            return 1/total
        return total