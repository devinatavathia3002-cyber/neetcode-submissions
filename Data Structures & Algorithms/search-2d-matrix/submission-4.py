class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # first, find which row our target is in

        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = (rows - 1)

        while l <= r:
            mid = ((r - l) // 2) + l

            curr = matrix[mid]
            start = curr[0]
            end = curr[cols - 1]

            if start <= target <= end:
                break
            elif target < start:
                r = mid - 1
            else:
                l = mid + 1
        
        finalRow = ((r - l) // 2) + l
        print(finalRow)
        l = 0
        r = cols - 1

        while l <= r:
            mid = ((r - l) // 2) + l

            curr = matrix[finalRow][mid]

            if target == curr:
                return True
            elif target < curr:
                r = mid - 1
            else:
                l = mid + 1
        
        return False



