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
        
        q = deque([(root,0,0)]) # node, row, col

        nodes = []

        while q:

            node, row, col = q.popleft()

            nodes.append((col,row, node.val))

            if node.left:
                q.append((node.left, row+1,col-1))
            if node.right:
                q.append((node.right,row+1, col+1))

        res = defaultdict(list)
        
        nodes.sort(key=lambda x: (x[0],x[1],x[2]))

        for col, row, val in nodes:
            res[col].append(val)
        
        return [res[c] for c in sorted(res)]



            
                


