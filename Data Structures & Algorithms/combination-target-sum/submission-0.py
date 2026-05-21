class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtracking(index, subset, total):
            nonlocal res

            if total == target:
                res.append(subset.copy())
                return
            if total > target:
                return

            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtracking(i, subset, total + nums[i])
                subset.pop()

        backtracking(0, [], 0)
        return res