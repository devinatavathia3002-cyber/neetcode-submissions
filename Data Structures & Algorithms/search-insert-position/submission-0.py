class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = ((r - l) // 2) + l
            val = nums[mid]

            if target > val:
                l = mid + 1
            elif target < val:
                r = mid - 1
            else:
                return mid


        # target wasn't found
        return l