# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validate(self, node, minimum, maximum):
        if node is None:
            return True
        
        if node.val > minimum and node.val < maximum:
            left = self.validate(node.left, minimum, node.val)
            right = self.validate(node.right, node.val, maximum)
            return left and right
            
        return False

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf'))