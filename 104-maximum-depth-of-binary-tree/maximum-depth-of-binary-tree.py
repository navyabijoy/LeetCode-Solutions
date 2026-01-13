# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.height = 0

    def traverse(self, root):
        if root is None:
            return 0
        
        leftHeight = self.traverse(root.left) + 1
        rightHeight =  self.traverse(root.right) + 1
        self.height = max(leftHeight, rightHeight)
        return self.height

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        self.traverse(root)
        return self.height