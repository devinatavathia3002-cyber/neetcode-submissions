class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        topCol = False
        topRow = False

        # mark first row/first col with 0
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    if c == 0:
                        topCol = True
                    if r == 0:
                        topRow = True
                    else:
                        matrix[0][c] = 0
                        matrix[r][0] = 0
        
        # update grid with 0s
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # check boolean
        if topCol:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        # check top row
        if topRow:
            for c in range(COLS):
                matrix[0][c] = 0
        
        