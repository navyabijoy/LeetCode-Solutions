# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        res = []
        queue = deque()
        queue.append(root) # store the entire node in queue
        leftToRight = True
        while len(queue) > 0:
            level_size = len(queue)
            level = [] # to store every level
            for _ in range(level_size):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            if not leftToRight:
                level.reverse()
            res.append(level)
            leftToRight = not leftToRight
        return res