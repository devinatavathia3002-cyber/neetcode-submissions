class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []
        
        def backtracking(num, subset):
            nonlocal res

            if len(subset) > k:
                return
            
            if len(subset) == k:
                res.append(subset.copy())
            
            for i in range(num, n + 1):
                subset.append(i)
                backtracking(i + 1, subset)
                subset.pop()

        backtracking(1, [])
        return res
