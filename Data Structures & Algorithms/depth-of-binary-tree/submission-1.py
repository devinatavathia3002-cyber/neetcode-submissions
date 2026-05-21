# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        amt = 0

        def maximum(node, count):
            nonlocal amt
            
            if not node:
                amt = max(amt, count)
                return
            
            maximum(node.right, count + 1)
            maximum(node.left, count + 1)
        
        maximum(root, 0)
        return amt