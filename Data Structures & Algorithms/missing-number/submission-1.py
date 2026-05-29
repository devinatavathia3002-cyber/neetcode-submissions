class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        
        for num in range(len(nums)):
            res = res ^ num ^ nums[num]

        return res