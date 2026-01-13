# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validate(self, root, minimum, maximum):
        if root is None:
            return True
        
        if root.val > minimum and root.val < maximum:
            left = self.validate(root.left, minimum, root.val)
            right = self.validate(root.right, root.val, maximum)
            return left and right
        
        return False
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf'))