class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l = 1
        r = max(piles)
        m = max(piles)

        while l < r:
            m = ((r - l) // 2) + l
            hours = 0

            hours = sum(math.ceil(p / m) for p in piles)
            
            if hours <= h:
                r = m
            else:
                l = m + 1

        return r