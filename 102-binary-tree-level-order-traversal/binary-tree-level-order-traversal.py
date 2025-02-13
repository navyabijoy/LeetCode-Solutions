# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res= []
        queue = deque()
        if not root:
            return []
        queue.append(root) 
        # store the whole node in queue as access left and right
        while len(queue) > 0:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                curr = queue.popleft()
                level.append(curr.val) # store only the value
                if curr.left is not None:
                    queue.append(curr.left) # store the whole node
                if curr.right is not None:
                    queue.append(curr.right)
            res.append(level)
        return res