# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (self.height(root) >= 0)

    def height(self, node):    
        if node is None:
            return 0
        leftHeight = self.height(node.left)
        rightHeight = self.height(node.right)
        if leftHeight < 0 or rightHeight < 0 or abs(leftHeight - rightHeight) >1:
            return -1
        return max(leftHeight, rightHeight) + 1
        