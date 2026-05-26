class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # recursive solution

        # def recurse(total, index):
        #     if total == target and index == len(nums):
        #         return 1
        #     if index == len(nums):
        #         return 0
            
        #     return recurse(total + nums[index], index + 1) + recurse(total - nums[index], index + 1)
        
        # return recurse(0, 0)


        # dp solution
        dp = defaultdict(int)
        dp[0] = 1

        for index in range(len(nums)):
            newDp = defaultdict(int)
            curr = nums[index]
            for num, ct in dp.items():
                newDp[num + curr] += ct
                newDp[num - curr] += ct
            dp = newDp
        
        return dp[target]



            