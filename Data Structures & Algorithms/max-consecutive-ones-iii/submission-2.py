class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxWindow = 0
        l, r = 0, 0
        leftover = k

        while r < len(nums):
            if nums[r] == 0:
                if leftover > 0:
                    leftover -= 1
                else:
                    maxWindow = max(maxWindow, r - l)
                    leftover -= 1
                    while l <= r and leftover < 0:
                        if nums[l] == 0:
                            leftover += 1
                        l += 1
            maxWindow = max(maxWindow, r - l + 1)
            r += 1

        return maxWindow