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
        
        q = deque([root])
        left_to_right = True
        res = []
        while q:
            level = []
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            if left_to_right:
                res.append(level)
            else:
                res.append(level[::-1])
            
            left_to_right = not left_to_right
        return res


