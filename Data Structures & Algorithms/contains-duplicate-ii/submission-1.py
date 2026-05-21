class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        l = 0
        r = 0

        q = set()

        while r < len(nums):

            if (r - l) > k:
                q.remove(nums[l])
                l += 1
            
            if nums[r] in q:
                return True
            
            q.add(nums[r])

            r += 1
        
        return False