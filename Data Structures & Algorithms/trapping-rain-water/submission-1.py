class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1
        maxArea = 0

        leftMax = height[l]
        rightMax = height[r]

        while l < r:

            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                area = (leftMax - height[l])

            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                area = (rightMax - height[r])
            
            if area > 0:
                maxArea += area


        return maxArea
        