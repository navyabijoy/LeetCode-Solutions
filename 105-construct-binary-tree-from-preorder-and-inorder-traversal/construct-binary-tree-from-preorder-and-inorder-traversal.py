# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findPosition(self, inorder, ele, n):
        for i in range(n):
            if inorder[i] == ele:
                return i
        return -1

    def solve(self, pre, inorder, inorderStart, inorderEnd, n):
        if self.index >= n or inorderStart > inorderEnd:
            return None
        ele = pre[self.index]  # in the initial call, get the root node val
        self.index += 1
        root = TreeNode(ele)  # create the root node
        pos = self.findPosition(inorder, ele, n)

        root.left = self.solve(pre, inorder, inorderStart, pos - 1, n)
        root.right = self.solve(pre, inorder, pos + 1, inorderEnd, n)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.index = 0
        n = len(inorder)
        ans = self.solve(preorder, inorder, 0, n - 1, n)
        return ans
