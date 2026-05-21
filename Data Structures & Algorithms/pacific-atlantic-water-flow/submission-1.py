class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])
        pac = set()
        atl = set()
        output = []

        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def dfs(row, col, ocean, prev):
            if (row < 0 or col < 0 
                or row >= ROWS or col >= COLS or
                (row, col) in ocean):
                return
            curr = heights[row][col]
            if prev > curr:
                return
            ocean.add((row, col))

            for direction in directions:
                dfs(row + direction[0], col + direction[1], ocean, curr)

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    dfs(r, c, pac, -1)
                if r == ROWS - 1 or c == COLS - 1:
                    dfs(r, c, atl, -1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    output.append([r, c])
        return output