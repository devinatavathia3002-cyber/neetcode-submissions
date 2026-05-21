# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def delLeaves(node):

            if not node:
                return None
            
            if node.val == target and node.right is None and node.left is None:
                return None
            
            node.right = delLeaves(node.right)
            node.left = delLeaves(node.left)

            if node.val == target and node.right is None and node.left is None:
                return None

            return node
        
        return delLeaves(root)