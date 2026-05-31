class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumOfSquares(slow)

        while slow != fast and slow != 1:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(self.sumOfSquares(fast))
        if slow == 1:
            return True
        return False

    def sumOfSquares(self, val):
        nextVal = 0
        while val > 0:
            last = val % 10
            val = val // 10

            nextVal += (last * last) 
        return nextVal