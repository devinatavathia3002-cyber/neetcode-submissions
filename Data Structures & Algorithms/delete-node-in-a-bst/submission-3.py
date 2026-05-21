# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        pointer = TreeNode(-1)
        pointer.right = root

        def traverse(node, key):
            if not node:
                return None
            
            if node.val == key:
                if node.right is None and node.left is None:
                    return None
            
                elif not node.right:
                    return node.left
                
                elif not node.left:
                    return node.right
                
                else:
                    curr = node
                    curr = curr.right
                    while curr.left:
                        curr = curr.left
                        
                    node.val, curr.val = curr.val, node.val

            node.right = traverse(node.right, key)
            node.left = traverse(node.left, key)

            return node

        traverse(pointer, key)
        return pointer.right