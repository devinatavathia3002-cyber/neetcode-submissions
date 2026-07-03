class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        maximum = len(nums) + 1
        # convert all negative numbers to 0s, or anything inconsequential
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = maximum
        
        # use array as hashmap marking
        for i in range(len(nums)):
            curr = abs(nums[i])
            if curr > 0 and curr < maximum:
                if nums[curr - 1] > 0:
                    nums[curr - 1] = -1 * nums[curr - 1]
            else:
                continue
        
        # return first missing positive
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:
                return i

        return maximum