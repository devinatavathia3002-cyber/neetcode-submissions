class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # greedy approach
        r, l = 0, 0
        n = len(nums)
        steps = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            steps += 1
            l = r + 1
            r = farthest

        return steps