# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([(root, 0)])
        max_width = 0

        while q:
            level_size = len(q)
            level_start, level_end = q[0][1], q[-1][1]
            max_width = max(max_width, level_end - level_start + 1)

            for _ in range(level_size):
                node, pos = q.popleft()
                if node.left:
                    q.append((node.left, pos * 2))
                if node.right:
                    q.append((node.right, pos * 2 + 1))
        return max_width
