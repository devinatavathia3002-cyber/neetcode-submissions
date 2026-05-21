# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        flag = True

        def dfs(node):
            nonlocal flag
            
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            # do true/false comparison here
            if abs(left - right) > 1:
                flag = False

            return max(left, right) + 1

        dfs(root) 
        return flag