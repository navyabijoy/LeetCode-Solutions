# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, node):
        if node is None:
            return 0
        left = self.height(node.left)
        right = self.height(node.right)
        return 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        # if root.left:
        left_bal = self.height(root.left)
        # if root.right:
        right_bal = self.height(root.right)
        
        if abs(left_bal - right_bal) > 1:
            return False
        
        return self.isBalanced(root.right) and self.isBalanced(root.left)
