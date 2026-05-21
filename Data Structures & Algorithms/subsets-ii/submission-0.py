class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        def backtracking(index, sub):
            nonlocal res
            res.append(sub.copy())

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                sub.append(nums[i])
                backtracking(i + 1, sub)
                sub.pop()

        backtracking(0, [])
        return res