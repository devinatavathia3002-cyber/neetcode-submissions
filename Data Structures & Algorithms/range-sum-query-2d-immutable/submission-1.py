class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROWS = len(matrix)
        self.COLS = len(matrix[0])
        self.sumMatrix = [[0] * (self.COLS + 1) for _ in range(self.ROWS + 1)]
        self.matrix = matrix

        for r in range(self.ROWS):
            total = 0
            for c in range(self.COLS):
                total += self.matrix[r][c]
                above = self.sumMatrix[r][c + 1]
                self.sumMatrix[r + 1][c + 1] = above + total 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        topLeft = self.sumMatrix[row1 - 1][col1 - 1]
        bottomRight = self.sumMatrix[row2][col2]

        above = self.sumMatrix[row1 - 1][col2]
        left = self.sumMatrix[row2][col1 - 1]

        return (bottomRight - above - left + topLeft)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)