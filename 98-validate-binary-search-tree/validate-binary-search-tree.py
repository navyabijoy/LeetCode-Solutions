# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []

        def inorder(node):
            if node is None:
                return None
                
            if node.left is not None:
                inorder(node.left)
            res.append(node.val)
            if node.right is not None:
                inorder(node.right)

        inorder(root)
        for i in range(1,len(res)):
            if res[i] <= res[i-1]:
                return False
        return True