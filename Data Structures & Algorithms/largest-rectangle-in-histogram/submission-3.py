class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # stack with map (index, height)
        s = []
        maxArea = 0

        for i in range(len(heights)):
            
            start = i
            while s and s[-1][1] > heights[i]:
                index, height = s.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            
            s.append((start, heights[i]))
        

        end = len(heights)
        while s:
            index, height = s.pop()
            maxArea = max(maxArea, height * (end - index))

        return maxArea

