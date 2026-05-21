class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        largest = grid[0][0]
        maxHeap = [] # value, coords
        visited = set()

        ROWS = len(grid)
        COLS = len(grid[0])

        heapq.heappush(maxHeap, [largest, (0, 0)])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while len(maxHeap) > 0:
            curr = heapq.heappop(maxHeap)
            val, coords = curr
            x = coords[0]
            y = coords[1]

            if coords in visited:
                continue
            visited.add((coords))
            largest = max(largest, val)

            if x == ROWS - 1 and y == COLS - 1:
                return largest

            for direction in directions:
                xCoord, yCoord = direction
                newX, newY = xCoord + x, yCoord + y
                if (newX < 0 or newY < 0 or 
                    newX >= ROWS or newY >= COLS or
                    (newX, newY) in visited):
                    continue
                heapq.heappush(maxHeap, [grid[newX][newY], (newX, newY)])
                