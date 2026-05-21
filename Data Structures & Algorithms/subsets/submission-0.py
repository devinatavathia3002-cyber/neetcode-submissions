class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subs = []

        def backtracking(index, subset):
            nonlocal subs

            for j in range(index, len(nums)):
                subset.append(nums[j])
                backtracking(j + 1, subset)
                subs.append(subset.copy())
                subset.pop()
        
        backtracking(0, [])
        subs.append([])
        return subs