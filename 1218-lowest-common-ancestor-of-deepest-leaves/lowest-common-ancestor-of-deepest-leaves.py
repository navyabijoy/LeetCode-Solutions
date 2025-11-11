# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if node is None:
            return None, 0  # node, depth

        left_node, left_depth = self.dfs(node.left)
        right_node, right_depth = self.dfs(node.right)

        if left_depth > right_depth:
            return left_node, left_depth + 1
        elif left_depth < right_depth:
            return right_node, right_depth + 1
        else:
            return node, left_depth + 1  # both equal, this node is LCA

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.dfs(root)[0]