class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = {}

        def recurse(total):
            if total in dp:
                return dp[total]
            if total == target:
                return 1
            if total > target:
                return 0
            
            dp[total] = 0
            for i in range(len(nums)):
                dp[total] += recurse(nums[i] + total)
            
            return dp[total]

        return recurse(0)