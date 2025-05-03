# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPaths(self, root,targetSum):
        if not root:
            return False

        count = 0
        if targetSum == root.val:
            count += 1
        
        count += self.countPaths(root.left, targetSum - root.val)
        count += self.countPaths(root.right, targetSum - root.val)
        
        return count

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        count = self.countPaths(root, targetSum)
        count += self.pathSum(root.left,targetSum)
        count += self.pathSum(root.right, targetSum)
        return count