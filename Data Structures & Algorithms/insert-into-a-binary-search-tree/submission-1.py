# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if root is None:
            root = TreeNode(val)
            return root
            
        pointer = root

        while True:
            if pointer.right is None and pointer.val < val:
                pointer.right = TreeNode(val)
                break
            elif pointer.left is None and pointer.val > val:
                pointer.left = TreeNode(val)
                break
            elif pointer.val < val:
                pointer = pointer.right
            else:
                pointer = pointer.left

        return root