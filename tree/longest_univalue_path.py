# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
      
        self.max_len = 0

        def dfs(node: TreeNode):
            if node is None:
                return 0

            left_len = dfs(node.left)
            right_len = dfs(node.right)

            left_side = 0
            if node.left and node.left.val == node.val:
                left_side = left_len + 1
            
            right_side = 0
            if node.right and node.right.val == node.val:
                right_side = right_len + 1
            
            self.max_len = max(self.max_len, left_side + right_side)

            return max(left_side, right_side)

        dfs(root)
        
        return self.max_len
