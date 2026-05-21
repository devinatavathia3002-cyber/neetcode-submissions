class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = defaultdict(int)
        suffix = defaultdict(int)

        cumulative = 1
        for i in range(len(nums)):
            prefix[i] = cumulative
            cumulative *= nums[i]
        
        multiply = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = multiply
            multiply *= nums[i]
        
        # final loop
        for i in range(len(nums)):
            nums[i] = (prefix[i] * suffix[i])
        

        return nums