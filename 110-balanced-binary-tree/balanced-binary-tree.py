# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def height(root):
            if root is None:
                return 0

            left_height = height(root.left) # does a dfs on the left nodes
            right_height = height(root.right) # does a dfs on the right nodes

            if abs(left_height - right_height) > 1:
                balanced[0] = False
                return 0

            return 1+max(left_height, right_height)
        
        height(root)
        return balanced[0]
