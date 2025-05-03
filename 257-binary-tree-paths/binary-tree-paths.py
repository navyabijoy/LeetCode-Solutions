# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, curr, res,path):
        if curr is None:
            return

        if curr.left is None and curr.right is None:
            res.append("->".join(path))
            return

        if curr.left:
            self.helper(curr.left,res,path + [str(curr.left.val)])
        if curr.right:
            self.helper(curr.right,res,path + [str(curr.right.val)])

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        res = []
        self.helper(root,res,[str(root.val)])
        return res