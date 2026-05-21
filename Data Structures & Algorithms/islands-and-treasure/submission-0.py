class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        visited = []
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visited.append([r, c])
                    q.append([r, c])
        
        def addCell(r, c):
            if 0 <= r < rows and 0 <= c < cols and [r, c] not in visited and grid[r][c] != -1:
                visited.append([r, c])
                q.append([r, c])
            else:
                return
        
        steps = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = steps

                addCell(row + 1, col)
                addCell(row - 1, col)
                addCell(row, col + 1)
                addCell(row, col - 1)

            steps += 1


