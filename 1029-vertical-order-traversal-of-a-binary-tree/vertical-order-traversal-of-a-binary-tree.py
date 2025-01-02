# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        level_items = defaultdict(list)
        queue = deque([(root, 0, 0)])
        min_col = float('inf')
        max_col = float('-inf')

        while queue:
            node, row, col = queue.popleft()

            if col < min_col:
                min_col = col

            if col > max_col:
                max_col = col

            level_items[col].append((node.val, row)) 
            # append the value of the node and row in that column

            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))
        res = []
        for level in range(min_col, max_col + 1):
            items = level_items[level]
            items.sort(key=lambda x: (x[1], x[0]))
            items = [val for val,_ in items]
            res.append(items)
        return res
