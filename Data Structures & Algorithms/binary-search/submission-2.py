class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            
            middle = ((r - l) // 2) + l
            if nums[middle] < target:
                l = l + 1
            elif nums[middle] > target:
                r = r - 1
            else:
                return middle
        
        return -1