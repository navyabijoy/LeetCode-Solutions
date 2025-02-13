# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,node):
        if node is None:
            return 0
        lefth = self.height(node.left)
        righth = self.height(node.right)
        return 1 + max(lefth, righth)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        lefth = self.isBalanced(root.left)
        righth = self.isBalanced(root.right)
        ans = abs(self.height(root.left) - self.height(root.right)) <= 1
        if lefth and righth and ans:
            return True
        else:
            return False