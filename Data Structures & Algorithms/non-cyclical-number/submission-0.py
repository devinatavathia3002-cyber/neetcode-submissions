class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        newVal = n

        while newVal not in seen and newVal != 1:
            nextVal = 0
            seen.append(newVal)
            while newVal > 0:
                last = newVal % 10
                newVal = newVal // 10

                nextVal += (last * last) 
            newVal = nextVal
        
        if newVal == 1:
            return True
        return False