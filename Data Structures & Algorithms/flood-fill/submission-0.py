class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        q = deque()
        q.append((sr, sc))

        orig = image[sr][sc]
        if orig == color:
            return image
            
        image[sr][sc] = color
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        ROWS = len(image)
        COLS = len(image[0])

        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for val in directions:
                    r, c = val
                    newRow = r + x
                    newCol = c + y
                    if newRow >= 0 and newRow < ROWS and newCol >= 0 and newCol < COLS and image[newRow][newCol] == orig:
                        image[newRow][newCol] = color
                        q.append((newRow, newCol))

        return image