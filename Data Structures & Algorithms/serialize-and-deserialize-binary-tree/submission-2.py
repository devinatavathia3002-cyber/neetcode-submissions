# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        q = deque([root])

        if root is None:
            return "N"

        while q:
            node = q.popleft()

            if node is not None:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)  
            else:
                res.append("N")
        
        return ",".join(res)

    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data[0] == "N":
            return None

        data = data.split(",")
        root = TreeNode(int(data[0]))
        q = deque([root])

        index = 0

        while q:
            curr = q.popleft()

            index += 1
            if data[index] != "N":
                curr.left = TreeNode(int(data[index]))
                q.append(curr.left)
            else:
                curr.left = None
            index += 1
            if data[index] != "N":
                curr.right = TreeNode(int(data[index]))
                q.append(curr.right)
            else:
                curr.right = None
            
        return root

