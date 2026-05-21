class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        # try this without caching 
        # first, find peak

        l, r = 0, mountainArr.length() - 2

        while l <= r:
            m = ((r - l) // 2) + l

            right = mountainArr.get(m + 1)
            left = mountainArr.get(m - 1)
            mid = mountainArr.get(m)

            if left < mid < right:
                # on left side
                l = m + 1
            elif left > mid > right:
                # on right side
                r = m - 1
            else:
                break
        
        peak = m
        peakVal = mountainArr.get(peak)
        if peakVal == target:
            return peak

        # search left side
        l, r = 0, peak - 1

        while l <= r:
            m = ((r - l) // 2) + l
            mid = mountainArr.get(m)

            if mid < target:
                l = m + 1
            elif mid > target:
                r = m - 1
            else:
                return m
        
        # search right side
        l, r = peak + 1, mountainArr.length() - 1

        while l <= r:
            m = ((r - l) // 2) + l
            mid = mountainArr.get(m)

            if mid < target:
                r = m - 1
            elif mid > target:
                l = m + 1
            else:
                return m
        
        return -1 