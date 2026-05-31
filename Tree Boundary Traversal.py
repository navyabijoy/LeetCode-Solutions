'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def traverseLeft(self, node):
        if (node is None) or (node.left is None and node.right is None):
            return 
            
        self.ans.append(node.data)
        
        if node.left:
            self.traverseLeft(node.left)
        else:
            self.traverseLeft(node.right)
            
    def traverseLeaf(self, node):
        if node is None:
            return
        
        if node.left is None and node.right is None:
            self.ans.append(node.data)
            return
        
        self.traverseLeaf(node.left)
        self.traverseLeaf(node.right)
    
    def traverseRight(self, node):
        if (node is None) or (node.left is None and node.right is None):
            return
        
        if node.right:
            self.traverseRight(node.right)
        else:
            self.traverseRight(node.left)
        
        self.ans.append(node.data)
        
    def boundaryTraversal(self, root):
        if not root:
            return []
            
        self.ans = []
        
        self.ans.append(root.data)
        self.traverseLeft(root.left)
        self.traverseLeaf(root.left)
        self.traverseLeaf(root.right)
        self.traverseRight(root.right)
        return self.ans
        
        
        
