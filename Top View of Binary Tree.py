'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque, defaultdict
class Solution:
    def topView(self, root):
        if root is None:
            return []
        
        q = deque([(root, 0)]) # root, level
        cols = defaultdict()
        min_col, max_col = 0, 0
        
        while q:
            node, col = q.popleft()
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            if col not in cols:
                cols[col] = node.data
            
            if node.left:
                q.append((node.left, col - 1))
            if node.right:
                q.append((node.right, col + 1))
        
        return [cols[c] for c in range(min_col, max_col+1)]
            
            
            
            
