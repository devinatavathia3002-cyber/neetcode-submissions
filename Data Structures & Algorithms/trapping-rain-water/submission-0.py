class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1

        maxLeft = height[l]
        maxRight = height[r]

        output = 0

        while l < r:
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])
            container = 0

            if maxLeft <= maxRight:
                container = (maxLeft - height[l])
                l += 1
            else:
                container = (maxRight - height[r])
                r -= 1
            if container > 0:
                output += container

        return output