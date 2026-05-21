class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        ROWS = len(heights)
        COLS = len(heights[0])
        minHeap = [[0, 0, 0]] # difference, r, c

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited = set()

        while minHeap:
            curr = heapq.heappop(minHeap)
            diff, r, c = curr
            if (r, c) in visited:
                continue
            visited.add((r, c))


            if r == ROWS - 1 and c == COLS - 1:
                return diff
            
            for direction in directions:
                row, col = direction
                newR, newC = row + r, col + c
                if (newR < 0 or newC < 0 or 
                    newR >= ROWS or newC >= COLS or
                    (newR, newC) in visited):
                    continue
                difference = max(diff, abs(heights[newR][newC] - heights[r][c]))
                heapq.heappush(minHeap, [difference, newR, newC])
