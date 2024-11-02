# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [root.val]

        def DFS(root):
            if root is None:
                return 0
            lmax = max(0, DFS(root.left))
            rmax = max(0, DFS(root.right))

            # Update the overall maximum path sum
            ans[0] = max(ans[0] , root.val + lmax + rmax)

            # Return the maximum path sum that starts from the current node
            return root.val + max(lmax , rmax)

            

        DFS(root)
        return ans[0]

        