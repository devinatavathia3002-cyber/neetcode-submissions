class Solution:
    def arrangeCoins(self, n: int) -> int:
        # (n/2) * (n + 1)
        l, r = 1, n
        res = 0

        while l <= r:
            mid = ((r - l) // 2) + l
            coins = mid * (mid + 1) // 2

            if coins > n:
                r = mid - 1
            elif coins < n:
                l = mid + 1
                res = mid
            else:
                return mid
        
        return res