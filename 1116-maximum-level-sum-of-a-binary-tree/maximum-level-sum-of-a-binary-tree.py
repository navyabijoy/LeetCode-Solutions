# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = []
        q = deque()
        q.append(root)

        max_sum = float('-inf')

        best_level = 1
        level = 1
        while q:
            level_sum = 0
            level_size = len(q)

            for _ in range(level_size):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                best_level = level
            
            level += 1
        return best_level


        
            

        



