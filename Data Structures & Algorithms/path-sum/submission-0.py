# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def hasPath(node, val):

            if not node:
                return False
            
            newSum = val + node.val
            if newSum == targetSum and node.right is None and node.left is None:
                return True
            
            return hasPath(node.right, val + node.val) or hasPath(node.left, val + node.val)
        
        if not root:
            return False
        return hasPath(root, 0)
            