class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
          
        rows = defaultdict(list)   
        cols = defaultdict(list)
        grid = defaultdict(list)

        for r in range(0, 9):
            for c in range(0, 9):
                if board[r][c] == ".":
                    continue
                
                val = board[r][c]
                
                # check rows
                if val in rows[r]:
                    return False
                rows[r].append(val)

                # check cols
                if val in cols[c]:
                    return False
                cols[c].append(val)

                # check 3x3 grid
                currR = (r // 3)
                currC = (c // 3)

                if val in grid[(currR, currC)]:
                    return False
                grid[(currR, currC)].append(val)



        return True