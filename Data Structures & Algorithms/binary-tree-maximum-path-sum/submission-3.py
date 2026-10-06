# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
    
        def divideAndConquer(node):
            if not node.left and not node.right:
                return (node.val, node.val)
            
            left_max_gain, right_max_gain = 0, 0
            max_pathSum_so_far = float("-inf")

            if node.left:
                left_max_through_root, left_max_so_far = divideAndConquer(node.left)
                if left_max_through_root > 0:
                    left_max_gain = left_max_through_root
                max_pathSum_so_far = max(max_pathSum_so_far, left_max_so_far)
            if node.right:
                right_max_through_root, right_max_so_far = divideAndConquer(node.right)
                if right_max_through_root > 0:
                    right_max_gain = right_max_through_root
                max_pathSum_so_far = max(max_pathSum_so_far, right_max_so_far)
            
            max_through_root_up = node.val + max(left_max_gain, right_max_gain) # The path can still extend the up of root
            max_through_root_stop = node.val + left_max_gain + right_max_gain # The path stops at the current root
            return (max_through_root_up, max(max_through_root_stop, max_pathSum_so_far))

        return divideAndConquer(root)[1]