class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()
        output = []

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, visited, prev):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            curr = heights[r][c]
            if prev > curr or (r, c) in visited:
                return
            
            visited.add((r, c))
            for num in directions:
                x, y = num
                dfs(r + x, c + y, visited, heights[r][c])
        

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0: # pacific
                    dfs(r, c, pac, heights[r][c])
                if r == rows - 1 or c == cols - 1: # atlantic
                    dfs(r, c, atl, heights[r][c])
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    output.append([r, c])

        return output