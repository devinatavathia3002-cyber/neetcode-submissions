# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        # root1, root2

        def dfs(node1, node2):
            if not node1 and not node2:
                return None
            if not node1:
                return node2
            if not node2:
                return node1
            
            curr = TreeNode(node1.val + node2.val)
            curr.right = dfs(node1.right, node2.right)
            curr.left = dfs(node1.left, node2.left)
            return curr
        
        return dfs(root1, root2)
            
            
        