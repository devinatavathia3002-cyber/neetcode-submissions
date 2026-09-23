class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        num, ct = 0, 0

        for read in range(len(nums)):
            if nums[read] != num:
                num = nums[read]
                ct = 1
            else:
                ct += 1

            if ct < 3:
                nums[write] = nums[read]
                write += 1

        return write