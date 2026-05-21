class Solution:
    def canJump(self, nums: List[int]) -> bool:

        dp = [False] * len(nums)
        dp[len(nums) - 1] = True

        for i in range(len(nums) - 2, -1, -1):
            val = nums[i]
            if val != 0:
                for j in range(i, i + val):
                    if dp[j + 1] == True:
                        dp[i] = True
                        break
        
        return dp[0]
        