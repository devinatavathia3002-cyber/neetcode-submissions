class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()

        def backtracking(index, subset, total):
            nonlocal res

            if total == target:
                res.append(subset.copy())
                return

            if total > target:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                subset.append(candidates[i])
                backtracking(i + 1, subset, total + candidates[i])
                subset.pop()

        backtracking(0, [], 0)
        return res