class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        l = 0
        r = 0

        output = [0] * k
        difference = float("infinity")

        testing = 0

        while r < len(arr):

            if (r - l + 1) > k:
                testing -= abs(x - arr[l])
                l += 1
            
            testing += abs(x - arr[r])

            if (r - l + 1) == k:
                if testing < difference:
                    difference = testing
                    output = arr[l:r+1]

            r += 1
        
        return output