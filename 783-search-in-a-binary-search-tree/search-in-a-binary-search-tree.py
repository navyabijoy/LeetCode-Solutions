# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return False
        temp = root
        while temp:
            if temp.val > val:
                temp = temp.left
            elif temp.val < val:
                temp = temp.right
            else:
                return temp
        return None