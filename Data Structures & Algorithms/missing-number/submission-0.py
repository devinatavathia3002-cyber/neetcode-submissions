class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for num in range(0, len(nums) + 1):
            nums.append(num)
        
        for num in nums:
            res = res ^ num

        return res