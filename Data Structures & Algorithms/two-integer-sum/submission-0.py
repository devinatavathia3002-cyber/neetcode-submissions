class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums) - 1):
            newTarget = target - nums[i]
            beg = i + 1
            end = len(nums) - 1
            mid = (end - beg)/2 + 1

            while beg <= end:
                if newTarget == nums[beg]:
                    array = [i, beg]
                    return array
                elif newTarget == nums[end]:
                    array = [i, end]
                    return array
                elif newTarget < mid:
                    beg += 1
                else:
                    end -= 1
        return

        