class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # recursive solution
        # def dfs(index, total):
            
        #     if total == target and index == len(nums):
        #         return 1
            
        #     if index >= len(nums):
        #         return 0
            
        #     return dfs(index + 1, total + nums[index]) + dfs(index + 1, total - nums[index])
        
        # return dfs(0, 0)

        # dp solution

        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            new = defaultdict(int)
            for total, count in dp.items():
                new[total + num] += count
                new[total - num] += count
            dp = new
        
        return dp[target]
