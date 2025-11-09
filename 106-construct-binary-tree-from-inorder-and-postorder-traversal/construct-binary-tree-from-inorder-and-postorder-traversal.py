# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createMapping(self, inorder, nodeToIndex, n):
        for idx, num in enumerate(inorder):
            nodeToIndex[num] = idx
        return nodeToIndex

    def solve(self, post, inorder, inorderStart, inorderEnd, n, nodeToIndex):
        if self.index < 0 or inorderStart > inorderEnd:
            return None
        ele = post[self.index]  # in the initial call, get the root node val
        self.index -= 1
        root = TreeNode(ele)  # create the root node
        pos = nodeToIndex[ele]

        root.right = self.solve(post, inorder, pos + 1, inorderEnd, n, nodeToIndex)
        root.left = self.solve(post, inorder, inorderStart, pos - 1, n, nodeToIndex)
        
        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        self.index = n - 1
        nodeToIndex = self.createMapping(inorder, {}, n)
        ans = self.solve(postorder, inorder, 0, n-1,n, nodeToIndex)
        return ans
