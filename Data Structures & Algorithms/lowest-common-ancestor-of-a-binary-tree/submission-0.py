# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        ans = root

        def LCA(node, p, q):
            nonlocal ans

            if not node:
                return False
            
            mid = (node.val == p.val or node.val == q.val)

            left = LCA(node.left, p, q)
            right = LCA(node.right, p, q)

            if mid + left + right >= 2:
                ans = node
            
            return mid or left or right

        LCA(root, p, q)
        return ans
        