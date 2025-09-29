# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([(root, 0, 0)])
        cols = []

        while q:
            node, col, row = q.popleft()
            cols.append((col, row, node.val))

            if node.left:
                q.append((node.left, col - 1, row + 1))
            if node.right:
                q.append((node.right, col + 1, row + 1))
            
        cols.sort(key=lambda x: (x[0], x[1], x[2]))

        res = defaultdict(list)

        for col, row, val in cols:
            res[col].append(val)

        return [res[c] for c in sorted(res)]