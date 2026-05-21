# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        maximum = -1000

        def findPaths(node):
            nonlocal maximum

            if not node:
                return 0

            right = max(findPaths(node.right), 0)
            left = max(findPaths(node.left), 0)

            maximum = max(maximum, left + right + node.val)

            return max(right, left) + node.val

        findPaths(root)
        return maximum