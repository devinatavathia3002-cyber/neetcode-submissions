# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkValid(node, minimum, maximum):

            if node is None:
                return True
            
            if node.val <= minimum or node.val >= maximum:
                return False
            
            right = checkValid(node.right, node.val, maximum)
            left = checkValid(node.left, minimum, node.val)
            
            return (right and left)
        
        return checkValid(root, -1001, 1001)
            
