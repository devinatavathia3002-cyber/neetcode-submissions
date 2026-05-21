class Solution:
    def mySqrt(self, x: int) -> int:
        
        # square root must be less than x // 2
        
        l = 0
        r = (x // 2)
        
        if x == 0 or x == 1:
            return x
        
        res = 1
        
        while l <= r:
            
            middle = ((r - l) // 2) + l
            
            if (middle * middle) < x:
                res = middle
                l = middle + 1
            elif (middle * middle) > x:
                r = middle - 1
            else:
                return middle
        return res