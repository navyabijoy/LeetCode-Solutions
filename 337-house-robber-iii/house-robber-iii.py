# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,curr,dp):
        if curr is None:
            return 0 

        if curr in dp:
            return dp[curr]

        # we have picked the root node
        pick = curr.val
        if curr.left:
            # we go to the grandchildren of node
            pick += self.helper(curr.left.left,dp) + self.helper(curr.left.right,dp) 
        if curr.right:
            pick += self.helper(curr.right.left,dp) + self.helper(curr.right.right,dp)

        # we have not picked the node
        notPick = self.helper(curr.left,dp) + self.helper(curr.right,dp)
        
        result = max(pick, notPick)
        dp[curr] = result
        return dp[curr]

    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None
        dp = {} # use hashmap for trees
        return self.helper(root,dp)
        