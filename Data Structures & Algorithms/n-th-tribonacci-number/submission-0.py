class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        num1, num2, num3 = 0, 1, 1

        for i in range(3, n + 1):
            new = num1 + num2 + num3
            num1, num2, num3 = num2, num3, new

        return num3