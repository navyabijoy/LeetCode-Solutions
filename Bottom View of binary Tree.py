'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''
from collections import defaultdict, deque

class Solution:
    def bottomView(self, root):
        if root is None:
            return []
        
        q = deque([(root, 0)])
        cols = defaultdict()
        min_col, max_col = 0, 0
        while q:
            node, c = q.popleft()
            min_col = min(min_col, c)
            max_col = max(max_col, c)
            
            cols[c] = node.data # keep overiding the value of that column, since its BFS the last value encountered is the bottom view
            
            if node.left:
                q.append((node.left, c - 1))
            if node.right:
                q.append((node.right, c + 1))
                
        return [cols[c] for c in range(min_col, max_col + 1)]
