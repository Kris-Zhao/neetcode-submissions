# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        if self.isSubtree(root.left, subRoot):
            return True

        if self.isSubtree(root.right, subRoot):
            return True
    
        return False

    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False

        return p.val == q.val and self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)