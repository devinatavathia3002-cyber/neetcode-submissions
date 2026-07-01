class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        vals = set()
        for num in nums:
            vals.add(num)
        
        missing = len(nums) + 1
        
        for i in range(1, len(nums) + 1):
            if i not in vals:
                return i

        return missing