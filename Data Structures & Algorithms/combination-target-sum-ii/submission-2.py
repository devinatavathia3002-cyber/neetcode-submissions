class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # subsets with target sum
        output = []
        candidates.sort()

        def subsets(i, total, sub):
            if total == target:
                output.append(sub.copy())
                return
            
            if total > target:
                return
            
            for j in range(i, len(candidates)):
                if j > 0 and candidates[j] == candidates[j - 1] and j != i:
                    continue
                sub.append(candidates[j])
                subsets(j + 1, total + candidates[j], sub)
                sub.pop()


        subsets(0, 0, [])
        return output