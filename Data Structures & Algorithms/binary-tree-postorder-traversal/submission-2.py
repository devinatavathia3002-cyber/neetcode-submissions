# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # result = []

        # def postorder(node):

        #     if not node:
        #         return
            
        #     postorder(node.left)
        #     postorder(node.right)
        #     result.append(node.val)

        
        # postorder(root)
        # return result

        # with a stack

        res = []
        stack = []
        cur = root

        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur.left)
                cur = cur.right
            else:
                cur = stack.pop()

        res.reverse()
        return res

