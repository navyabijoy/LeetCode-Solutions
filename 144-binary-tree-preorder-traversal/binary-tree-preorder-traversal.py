# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse(node):
            if node is None:
                return 
            res.append(node.val)
            if node.left is not None:
                traverse(node.left)
            if node.right is not None:
                traverse(node.right)
        traverse(root)
        return res