class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1
        mostWtr = 0

        while left != right:
            container = (right - left) * min(heights[right], heights[left])
            if heights[right] <= heights[left]:
                right -= 1
            else:
                left += 1
            
            mostWtr = max(container, mostWtr)

        
        return mostWtr