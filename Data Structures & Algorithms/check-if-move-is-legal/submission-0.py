class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        # always need that directions array girliees
        directions = {
            "R": (0, 1),
            "D": (1, 0),
            "L": (0, -1),
            "U": (-1, 0),
            "URD": (-1, 1),
            "ULD": (-1, -1),
            "BRD": (1, 1),
            "BLD": (1, -1)
        }
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, ct, direction):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == ".":
                print((r, c))
                print("first")
                return False
            
            if ct >= 3 and board[r][c] == color:
                return True
            
            if ct == 2 and board[r][c] == color:
                print((r, c))
                return False
            
            new_r, new_c = r + directions[direction][0], c + directions[direction][1]
            if dfs(new_r, new_c, ct + 1, direction):
                return True
            
            return False

        for key, val in directions.items():
            x, y = val
            new_r, new_c = rMove + x, cMove + y
            if dfs(new_r, new_c, 2, key):
                    return True

        return False