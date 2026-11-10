class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonic stack, as long as the bars are increasing in height, add to stack
        # add in (height, index)
        # once we reach a height lower than the last, pop off until we reach a height lower 
        # than the current height, add it into the stack with that popped index

        longest = 0
        stack = []

        for i in range(len(heights)):
            curr = heights[i]
            if not stack or stack[-1][0] < curr:
                stack.append((curr, i))
            else:
                start, end = i, i
                while stack and stack[-1][0] > curr:
                    height, index = stack.pop()
                    longest = max(longest, height * (end - index))
                    start = index
                stack.append((curr, start))
        
        if stack:
            while stack:
                height, index = stack.pop()
                longest = max(longest, height * (len(heights) - index))

        return longest