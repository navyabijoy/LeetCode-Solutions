# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node, counter, k , k_smallest):
            if not node or counter[0] >= k:
                return
            inorder(node.left, counter,k,k_smallest )
            
            counter[0] += 1 # after every traversal increase the value of counter

            if counter[0] == k: # if counter is k
                k_smallest[0] = node.val
                return

            inorder(node.right, counter, k,k_smallest)
        
        k_smallest = [float('inf')]
        counter = [0]
        inorder(root, counter, k,k_smallest)
        return k_smallest[0]
