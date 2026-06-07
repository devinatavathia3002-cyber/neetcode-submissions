class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        topCol = False
        topRow = False

        # set 0 markers
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    if r == 0:
                        topRow = True
                    if c == 0:
                        topCol = True
                    else:
                        matrix[r][0] = 0
                        matrix[0][c] = 0
                else:
                    continue
        
        # set almost all 0s
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                else:
                    continue
        
        # check booleans
        if topCol:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        if topRow:
            for c in range(COLS):
                matrix[0][c] = 0


        