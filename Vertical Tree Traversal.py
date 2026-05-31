'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def verticalOrder(self, root): 
        if root is None:
            return []
        
        # BFS - so that levels update clearly
        # in bfs we use queue
        q = deque([(root, 0)]) # node, level
        min_col, max_col = 0, 0
        cols = defaultdict(list)
        
        while q:
            node, col = q.popleft()
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            cols[col].append(node.data)
            
            if node.left:
                q.append((node.left, col - 1)) # col decreases when it moves left
            
            if node.right:
                q.append((node.right, col + 1))
            
        return [cols[c] for c in range(min_col, max_col + 1)]
        
        
        
