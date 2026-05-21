"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

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