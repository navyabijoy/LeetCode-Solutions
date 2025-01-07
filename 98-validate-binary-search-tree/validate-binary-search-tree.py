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
                 # inorder is supposed to write the array in ascending order for BST
                 # now if the number before the current number is greater than the current number
                 # then the tree is NOT bst
                return False
        return True