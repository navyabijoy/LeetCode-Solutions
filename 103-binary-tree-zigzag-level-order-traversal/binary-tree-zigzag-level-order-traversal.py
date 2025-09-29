# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if root is None:
            return res

        q = deque()
        q.append(root)

        leftToRight = True

        while q:
            level_size = len(q)
            level = [0] * level_size

            for i in range(level_size):
                frontNode = q.popleft()
                index = i if leftToRight else level_size - i - 1
                level[index] = frontNode.val

                if frontNode.left:
                    q.append(frontNode.left)
                if frontNode.right:
                    q.append(frontNode.right)
            
            leftToRight = not leftToRight

            res.append(level)
        
        return res