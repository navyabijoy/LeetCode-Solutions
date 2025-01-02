# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def right(node, level, res):
            if node is None:
                return
            if level == len(res):
                res.append(node.val)
            right(node.right, level+1,res)
            right(node.left, level+1,res)

        right(root,0,res)
        return res