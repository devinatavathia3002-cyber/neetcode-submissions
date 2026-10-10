class Solution:
    def totalNQueens(self, n: int) -> int:
        
        # I think for this version we can return the answer inside the function itself
        # (no global variable)

        cols = set()
        pos = set()
        neg = set()

        def backtrack(r):
            if r >= n:
                return 1
            
            res = 0
            for c in range(n):
                if c not in cols and (r + c) not in pos and (r - c) not in neg:
                    cols.add(c)
                    pos.add(r + c)
                    neg.add(r - c)

                    res += backtrack(r + 1)

                    cols.remove(c)
                    pos.remove(r + c)
                    neg.remove(r - c)

            return res
        

        return backtrack(0)