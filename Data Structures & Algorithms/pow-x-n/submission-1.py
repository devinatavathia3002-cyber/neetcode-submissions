class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        counter = 1
        total = 1
        while counter <= (abs(n) // 2):
            total *= x
            counter += 1
        
        if n % 2 != 0:
            if n < 0:
                return 1/(total * total * x)
            return total * total * x
        
        if n < 0:
            return 1/(total * total)
        return total * total

        