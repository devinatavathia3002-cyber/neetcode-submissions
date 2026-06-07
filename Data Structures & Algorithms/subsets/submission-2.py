class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        output = [[]]

        def recurse(i, curr):
            if i == len(nums):
                return
            
            for j in range(i, len(nums)):
                curr.append(nums[j])
                recurse(j + 1, curr)
                output.append(curr.copy())
                curr.pop()

        recurse(0, [])
        return output