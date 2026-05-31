class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l, r = 0, COLS - 1
        top, bottom = 0, ROWS - 1

        res = []

        while l <= r and top <= bottom:

            # get top row
            for i in range(l, r + 1):
                res.append(matrix[top][i])
            top += 1

            # get rightmost column
            for i in range(top, bottom + 1):
                res.append(matrix[i][r])
            r -= 1

            if not (l <= r and top <= bottom):
                break
                
            # get bottom row
            for i in range(r, l - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

            # get leftmost column
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][l])
            l += 1

        return res