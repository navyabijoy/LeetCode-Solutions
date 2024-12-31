# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.preOrder(root, res)
        return res
        
    def preOrder(self, root, res):
        if root is None:
            return None
        res.append(root.val)
        self.preOrder(root.left, res)
        self.preOrder(root.right, res)