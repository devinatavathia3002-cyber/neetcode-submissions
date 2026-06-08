class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # recursive solution
        # def recurse(index):
        #     if index >= len(nums):
        #         return 0
            
        #     return max(nums[index] + recurse(index + 2), recurse(index + 1))
        
        # return recurse(0)

        # dp solution
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        dpIndex = 2
        for i in range(1, len(nums)):
            curr = nums[i]
            dp[dpIndex] = max(dp[dpIndex - 1], curr + dp[dpIndex - 2])
            dpIndex += 1

        return dp[len(nums)]