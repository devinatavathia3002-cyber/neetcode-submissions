class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 4:
            if len(nums) == 3:
                return max(nums[1], max(nums[0], nums[2]))
            if len(nums) == 2:
                return max(nums[0], nums[1])
            if len(nums) == 1:
                return nums[0]
        
        def helper(start, end):
            first = nums[start]
            second = max(nums[start], nums[start + 1])

            for i in range(start + 2, end):
                temp = second
                second = max(second, first + nums[i])
                print(second)
                first = temp
            
            return second

        return max(helper(0, len(nums) - 1), helper(1, len(nums)))