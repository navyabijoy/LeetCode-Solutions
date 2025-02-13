# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,node,maxi):
        if node is None:
            return 0
        lefth = self.height(node.left,maxi)
        righth = self.height(node.right,maxi)
        maxi[0] = max(maxi[0], lefth + righth)  # Update the maximum diameter
        return 1 + max(lefth,righth)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = [0]
        self.height(root,maxi)
        return maxi[0]