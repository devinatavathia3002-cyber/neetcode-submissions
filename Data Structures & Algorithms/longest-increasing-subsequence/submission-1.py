class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # def dfs(pre, index):
        #     if index >= len(nums):
        #         return 0
        #     val = nums[index]
        #     if val > pre:
        #         return max(dfs(val, index + 1) + 1, dfs(pre, index + 1))
        #     return dfs(pre, index + 1)
        
        # return dfs(float("-inf"), 0)

        # with dp
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            curr = nums[i]
            for j in range(i + 1, len(nums)):
                if curr >= nums[j]:
                    continue
                dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
