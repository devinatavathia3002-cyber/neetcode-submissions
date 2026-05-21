class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            index = abs(nums[i])
            if nums[index] < 0:
                return index

            nums[index] = -1 * nums[index]
            