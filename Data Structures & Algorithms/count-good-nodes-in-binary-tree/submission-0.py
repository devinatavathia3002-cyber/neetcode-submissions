# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
    
        def track(node, greatest):

            curr = 1

            if not node:
                return 0
            
            if node.val < greatest.val:
                curr = 0
            
            if node.val > greatest.val:
                greatest = node
            
            return (track(node.right, greatest)) + (track(node.left, greatest)) + curr
        
        return track(root, TreeNode(-200))
        
