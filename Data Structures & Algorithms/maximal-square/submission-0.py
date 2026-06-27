class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = defaultdict(int)

        def counting(r, c):
            if (r, c) in dp:
                return dp[(r, c)]

            if 0 <= r < ROWS and 0 <= c < COLS and matrix[r][c] != "0":
                dp[(r, c)] = 1 + min(
                    counting(r + 1, c),
                    counting(r, c + 1),
                    counting(r + 1, c + 1)
                )
                return dp[(r, c)]
            return 0

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, counting(r, c))
        return res * res




