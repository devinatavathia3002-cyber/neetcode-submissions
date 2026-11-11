class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # [1, 1, 2, 2, 4, 5, 6, 9]
        candidates.sort()
        res = []

        def backtrack(i, sub):
            total = sum(sub)

            if total == target:
                print(sub)
                res.append(sub.copy())
                return
            
            if total > target:
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                sub.append(candidates[j])
                backtrack(j + 1, sub)
                sub.pop()

        backtrack(0, [])
        return res