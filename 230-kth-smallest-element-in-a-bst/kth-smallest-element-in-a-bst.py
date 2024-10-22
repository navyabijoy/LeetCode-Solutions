# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def traverse(current_node, k):
            if current_node is None:
                return None
            left = traverse(current_node.left, k)

            if left:
                return left
            k[0] -= 1
            if k[0] == 0:
                return current_node
            return traverse(current_node.right, k)

        return traverse(root, [k]).val