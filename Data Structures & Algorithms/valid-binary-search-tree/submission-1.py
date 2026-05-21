# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(node, mini, maxi):
            if not node:
                return True

            if node.val <= mini or node.val >= maxi:
                return False
            
            right = isValid(node.right, node.val, maxi)
            left = isValid(node.left, mini, node.val)

            return right and left
        
        return isValid(root, -1000, 1000)

