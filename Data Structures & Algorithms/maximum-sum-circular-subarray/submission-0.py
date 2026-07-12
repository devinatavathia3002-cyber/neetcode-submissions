class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = 0
        globalMax = nums[0]

        currMin = 0
        globalMin = nums[0]

        total = 0

        for num in nums:
            currMax = max(num, num + currMax)
            globalMax = max(globalMax, currMax)

            currMin = min(num, num + currMin)
            globalMin = min(globalMin, currMin)

            total += num
        
        if total < 0:
            return globalMax
        return max((total - globalMin), globalMax)