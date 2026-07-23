class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # binary search
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = ((r - l) // 2) + l
            if ((mid + 1) == len(nums) or nums[mid + 1] != nums[mid]) and (mid == 0 or nums[mid - 1] != nums[mid]):
                return nums[mid]
            else:
                if mid > 0 and nums[mid - 1] == nums[mid]:
                    left = (mid - 1)
                    if left % 2:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    left = (mid)
                    if left % 2:
                        r = mid - 1
                    else:
                        l = mid + 1
        return -1