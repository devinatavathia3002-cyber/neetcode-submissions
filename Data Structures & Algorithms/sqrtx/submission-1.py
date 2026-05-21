class Solution:
    def mySqrt(self, x: int) -> int:
        
        # square root must be less than x // 2
        
        l = 0
        r = (x // 2)
        
        if x == 0 or x == 1:
            return x
        
        while l <= r:
            
            middle = ((r - l) // 2) + l
            
            if (middle * middle) < x and ((middle + 1) * (middle + 1)) > x:
                return middle
            if (middle * middle) < x:
                l = middle + 1
            elif (middle * middle) > x:
                r = middle - 1
            else:
                return middle
        