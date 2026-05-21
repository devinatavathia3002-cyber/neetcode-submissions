class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        
        while l < r:
            m = ((r - l) // 2) + l # right-biased midpoint
            
            if abs(x - arr[m]) <= abs(x - arr[m + k]):
                r = m
            else:
                l = m + 1
                
        return arr[l:l+k]