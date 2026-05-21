class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # initialize prefix array
        prefix = [0] * len(nums)
        prefix[0] = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]
        
        # initialize suffix array
        suffix = [0] * len(nums)
        suffix[len(nums) - 1] = nums[len(nums) - 1]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]
        

        # FINAL for loop
        for i in range(len(nums)):
            if i == 0:
                nums[i] = 1 * suffix[i + 1]
            elif i == len(nums) - 1:
                nums[i] = 1 * prefix[i - 1]
            else:
                nums[i] = prefix[i - 1] * suffix[i + 1]
    
        return nums


