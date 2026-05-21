class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        l = 0
        r = 0

        q = deque()

        while r < len(nums):

            if (r - l) > k:
                q.popleft()
                l += 1
            
            if nums[r] in q:
                return True
            
            q.append(nums[r])

            r += 1
        
        return False