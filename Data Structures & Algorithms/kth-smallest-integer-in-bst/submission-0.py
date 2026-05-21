# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # in order traversal
        top = k

        def inorder(node):
            nonlocal top

            if node is None:
                return None

            left = inorder(node.left)
            if left is not None:
                return left
            
            top -= 1
            if top == 0:
                return node.val
            
            return inorder(node.right)
        
        return inorder(root)