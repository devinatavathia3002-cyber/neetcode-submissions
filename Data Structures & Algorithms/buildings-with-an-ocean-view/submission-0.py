class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        output = []

        for i in range(len(heights) - 1, -1, -1):
            curr = heights[i]
            while stack and stack[-1] < curr:
                stack.pop()
            if len(stack) == 0:
                output.append(i)
            stack.append(curr)
        
        return output[::-1]