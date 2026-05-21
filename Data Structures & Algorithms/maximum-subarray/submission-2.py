class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return sum(nums)
        
        total = 0
        best = nums[0]
        for num in nums:
            total = max(num, num + total)
            best = max(total, best)

        return best