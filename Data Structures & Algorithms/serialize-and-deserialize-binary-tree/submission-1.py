# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("#")

        return ",".join(res)
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        
        res = data.split(",")
        root = TreeNode(int(res[0]))
        queue = deque([root])
        i = 1

        while queue:
            node = queue.popleft()

            if res[i] != "#":
                node.left = TreeNode(int(res[i]))
                queue.append(node.left)
            i += 1

            if res[i] != "#":
                node.right = TreeNode(int(res[i]))
                queue.append(node.right)
            i += 1

        return root