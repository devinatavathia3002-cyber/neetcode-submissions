class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num

        while l <= r:
            mid = ((r - l) // 2) + l
            square = mid * mid

            if square < num:
                l = mid + 1
            elif square > num:
                r = mid - 1
            else:
                return True
        
        return False