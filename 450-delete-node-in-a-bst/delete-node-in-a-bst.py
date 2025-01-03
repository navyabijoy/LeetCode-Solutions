# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root

        # find the node to delete
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            #we have found the node
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            #find the min from right subtree
            curr = root.right
            while curr.left:
                curr = curr.left # go to the left most node
            root.val = curr.val # root is the node that is supposed to be deleted
            root.right = self.deleteNode(root.right, root.val)
        return root


        
        