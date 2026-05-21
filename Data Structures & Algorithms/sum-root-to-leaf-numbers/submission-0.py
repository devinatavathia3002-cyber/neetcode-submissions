# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        res = []
        total = 0

        def findPaths(node, path):
            nonlocal res

            if not node:
                return
            
            path += str(node.val)
            
            findPaths(node.right, path)
            findPaths(node.left, path)

            if node.right is None and node.left is None:
                res.append(path)

            path[:-1]
        
        findPaths(root, "")

        for num in res:
            num = int(num)
            total += num

        return total
