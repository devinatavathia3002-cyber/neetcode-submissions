class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # first, search through rows
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = rows - 1
        c = cols - 1

        rowIndex = 0

        while l <= r:
            m = ((r - l) // 2) + l
            curr = matrix[m]

            if target >= matrix[m][0] and target <= matrix[m][c]:
                rowIndex = m
                break
            elif target < matrix[m][0]:
                r = m - 1
            else:
                l = m + 1
        
        l = 0
        r = len(matrix[rowIndex]) - 1

        while l <= r:
            m = ((r - l) // 2) + l
            curr = matrix[rowIndex]
            
            print(l)
            print(r)
            if target == curr[m]:
                return True
            elif target < curr[m]:
                r = m - 1
            else:
                l = m + 1
        
        return False
