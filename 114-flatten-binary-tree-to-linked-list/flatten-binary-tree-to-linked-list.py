# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        temp = root
        while temp:
            if temp.left:
                last = temp.left

                while last.right:
                    last = last.right
                last.right = temp.right
                temp.right = temp.left
                temp.left = None
            temp = temp.right
        return temp