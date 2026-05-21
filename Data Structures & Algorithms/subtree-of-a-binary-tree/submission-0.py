# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def compare(node, subRoot):
            if not node:
                return False

            if node:
                if node.val == subRoot.val:
                    if isSame(node, subRoot):
                        return True
            return compare(node.right, subRoot) or compare(node.left, subRoot)

        def isSame(p1, p2):
            if p1 is None and p2 is None:
                return True
            if p1 is None:
                return False
            if p2 is None:
                return False
            
            if p1.val != p2.val:
                return False
            
            return isSame(p1.right, p2.right) and isSame(p1.left, p2.left)
        
        return compare(root, subRoot)