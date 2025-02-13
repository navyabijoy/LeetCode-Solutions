# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalancedFast(self,node):
        if node is None:
            return (True,0)

        left = self.isBalancedFast(node.left)
        right = self.isBalancedFast(node.right)
        leftAns = left[0]
        rightAns = right[0]
        diff = abs(left[1] - right[1]) <= 1
        height = max(left[1], right[1]) + 1
        isBalanced = leftAns and rightAns and diff
        return (isBalanced, height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedFast(root)[0]