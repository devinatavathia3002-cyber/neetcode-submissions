class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        # rows
        for r in range(ROWS):
            total = sum(grid[r])
            if total <= 1:
                continue
            res += total
            for c in range(COLS):
                if grid[r][c] == 1:
                    grid[r][c] = -1

        # cols
        for c in range(COLS):
            col_sum = 0
            unmarked = 0
            for r in range(ROWS):
                if abs(grid[r][c]) > 0:
                    if grid[r][c] < 0:
                        col_sum += 1
                    else:
                        unmarked += 1
                        col_sum += 1
            if col_sum > 1:
                res += unmarked
        return res