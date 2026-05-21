class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        r = sum(weights)
        l = max(weights)

        while l < r:

            m = ((r - l) // 2) + l
            totalW = 0
            daysC = 0

            for weight in weights:
                if totalW + weight > m:
                    daysC += 1
                    totalW = weight
                else:
                    totalW += weight
            
            if totalW > 0:
                daysC += 1
            
            if daysC <= days:
                r = m
            else:
                l = m + 1

        return r