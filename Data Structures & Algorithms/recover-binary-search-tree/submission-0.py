# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # first do the inorder traversal
        # [3, 2, 1]
        # [1, 3, 2, 4]
        if not root:
            return None
        
        sortedList = []
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            sortedList.append(node)
            inorder(node.right)
        
        inorder(root)
        node1, node2 = None, None
        for i in range(len(sortedList) - 1):
            if sortedList[i].val >= sortedList[i + 1].val:
                if node1:
                    node2 = sortedList[i + 1]
                else:
                    node1, node2 = sortedList[i], sortedList[i + 1]
        

        print(node1, node2)
        node1.val, node2.val = node2.val, node1.val
