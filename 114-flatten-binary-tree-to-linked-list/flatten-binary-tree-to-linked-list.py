# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        temp = root
        while temp:
            if temp.left:
                last = temp.left

                while last.right:
                    last = last.right
                last.right = temp.right
                temp.right = temp.left
                temp.left = None
            temp = temp.right
        return temp

    '''
    Traverse the binary tree, and for each node, check if it has a left child.
    If the left child exists, find the rightmost node in the left subtree.
    Point the right pointer of the rightmost node to the right child of the current node.
    Set the current node’s right pointer to the current node’s left pointer.
    Set the current node’s left child to NULL.
    Repeat the steps above until the entire binary tree has been traversed.
    '''