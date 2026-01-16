# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def count(self, node):
        if node is None:
            return 0
        
        left = self.count(node.left)
        right = self.count(node.right)
        total = left + right + 1
        return total

    def countNodes(self, root: Optional[TreeNode]) -> int:
        summ = self.count(root)
        return summ
        