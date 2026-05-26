class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # recursive solution

        def recurse(total, index):
            if total == target and index == len(nums):
                return 1
            if index == len(nums):
                return 0
            
            return recurse(total + nums[index], index + 1) + recurse(total - nums[index], index + 1)
        
        return recurse(0, 0)

            