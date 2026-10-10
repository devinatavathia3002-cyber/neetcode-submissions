class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # mapping for each col to a set of queen (r, c) placements
        # mapping for each pos diagonal to a set of queen (r, c) placements
        # same for neg diagonal ^^

        cols = set()
        pos = set()
        neg = set()

        allBoards = []

        def backtrack(r, board):
            if r >= n:
                allBoards.append(["".join(r) for r in board])
                return 
            
            else:
                for col in range(n):
                    if (r - col) not in neg and (r + col) not in pos and col not in cols:
                        board[r][col] = "Q"
                        cols.add(col)
                        pos.add(r + col)
                        neg.add(r - col)

                        backtrack(r + 1, board)

                        board[r][col] = "."
                        pos.remove(r + col)
                        neg.remove(r - col)
                        cols.remove(col)
            return
        
        board = [["."] * n for _ in range(n)]
        
        backtrack(0, board)
        return allBoards

