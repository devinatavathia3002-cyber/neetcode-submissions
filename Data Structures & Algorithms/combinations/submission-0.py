class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # make array from 1 - n
        nums = []
        res = []

        for i in range(1, n + 1):
            nums.append(i)
        
        def backtracking(index, subset):
            nonlocal res
            nonlocal nums

            if len(subset) > k:
                return
            
            if len(subset) == k:
                res.append(subset.copy())
            
            for i in range(index, len(nums)):
                subset.append(nums[i])
                backtracking(i + 1, subset)
                subset.pop()

        backtracking(0, [])
        return res
