class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # if len(nums) == 1:
        #     return nums[0]
        
        # dp = [0] * len(nums)
        # dp[0] = nums[0]
        # dp[1] = max(nums[1], nums[0])

        # for i in range(2, len(nums)):
        #     # skip, or take it
        #     dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        # return dp[-1]

        # now with no extra space

        if len(nums) == 1:
            return nums[0]
        
        first, second = nums[0], max(nums[1], nums[0])

        for i in range(2, len(nums)):
            temp = second
            second = max(second, first + nums[i])
            first = temp
        
        return second

