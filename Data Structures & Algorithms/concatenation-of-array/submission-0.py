class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        final = [0] * (2 * len(nums))
        n = len(nums)

        for i in range(n):
            final[i] = nums[i]
            final[i + n] = nums[i]
        
        return final
