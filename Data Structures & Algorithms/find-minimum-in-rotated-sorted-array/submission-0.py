class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # find the drop (point of rotation)
        l = 0
        r = len(nums) - 1
        last = nums[r]

        while l < r:
            m = ((r - l) // 2) + l

            if nums[m] > last:
                l = m + 1
            else:
                r = m

        return nums[r]