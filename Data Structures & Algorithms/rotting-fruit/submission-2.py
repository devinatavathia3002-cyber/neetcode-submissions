class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        output = 0
        fresh = 0
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
                    
        while q and fresh > 0:
            for val in range(len(q)):
                row, col = q.popleft()
                if row > 0:
                    if grid[row - 1][col] == 1:
                        fresh -= 1
                        grid[row - 1][col] = 2
                        q.append((row - 1, col))
                if row < rows - 1:
                    if grid[row + 1][col] == 1:
                        fresh -= 1
                        grid[row + 1][col] = 2
                        q.append((row + 1, col))
                if col > 0:
                    if grid[row][col - 1] == 1:
                        fresh -= 1
                        grid[row][col - 1] = 2
                        q.append((row, col - 1))
                if col < cols - 1:
                    if grid[row][col + 1] == 1:
                        fresh -= 1
                        grid[row][col + 1] = 2
                        q.append((row, col + 1))
            output += 1
                    
        return output if fresh == 0 else -1

