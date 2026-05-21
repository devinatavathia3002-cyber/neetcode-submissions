class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        numRows = len(board)
        numCols = len(board[0])

        rows = defaultdict(list)
        cols = defaultdict(list)
        grid = defaultdict(list)

        for r in range(numRows):
            for c in range(numCols):

                curr = board[r][c]

                if curr == ".":
                    continue

                if curr in rows[r]:
                    return False
                if curr in cols[c]:
                    return False
                if curr in grid[( r // 3, c // 3)]:
                    return False

                rows[r].append(curr)
                cols[c].append(curr)
                grid[( r // 3, c // 3)].append(curr)

        return True