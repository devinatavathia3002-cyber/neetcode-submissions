# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        preIndex = 0
        indices = {val: idx for idx, val in enumerate(inorder)}

        def divide(l, r):
            nonlocal preIndex

            if l > r:
                return None

            node = TreeNode(preorder[preIndex])
            mid = indices.get(node.val)
            preIndex += 1

            node.left = divide(l, mid - 1)
            node.right = divide(mid + 1, r)

            return node
        
        return divide(0, len(preorder) - 1)