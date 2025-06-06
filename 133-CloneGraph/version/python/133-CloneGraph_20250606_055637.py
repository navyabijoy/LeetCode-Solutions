# Last updated: 6/6/2025, 5:56:37 AM
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def helper(self,root, nodes_completed):
        if not root:
            return None
        
        copy = Node(root.val) 
        nodes_completed[root] = copy

        for p in root.neighbors:
            # if p is already cloned, get extract that 
            x = nodes_completed.get(p)
            # if p is not cloned, we recursively clone it
            if not x:
                copy.neighbors += [self.helper(p, nodes_completed)]
            else:
                copy.neighbors += [x]
        return copy

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodes_completed = {}
        return self.helper(node, nodes_completed)