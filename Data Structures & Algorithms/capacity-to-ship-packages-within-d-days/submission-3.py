class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # range for BS max(weights) -> sum(weights)
        l, r = max(weights), sum(weights)
        res = r

        def isValid(capacity):
            limit = capacity
            ships = 1

            for w in weights:
                if limit - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    limit = capacity
                limit -= w
            return True

        while l <= r:
            mid = ((r - l) // 2) + l
            if isValid(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res