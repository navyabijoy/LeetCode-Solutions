# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createParentMapping(self,root,start,nodeToParent):
        
        res = None
        q = deque()
        q.append(root)
        nodeToParent[root] = None

        while q:
            front = q.popleft()
            if front.val == start:
                res = front

            if front.left:
                nodeToParent[front.left] = front
                q.append(front.left)

            if front.right:
                nodeToParent[front.right] = front
                q.append(front.right)
        
        return res

    def infectTree(self, root,target, nodeToParent):
        visited = {}
        q = deque()
        ans = 0
        q.append(target)
        visited[target] = True
        while q:
            flag = False
            level = len(q)

            for _ in range(level):
                
                front = q.popleft()

                if front.left and front.left not in visited:
                    visited[front.left] = True
                    q.append(front.left)
                    flag = True

                if front.right and front.right not in visited:
                    visited[front.right] = True
                    q.append(front.right)
                    flag = True
                
                if nodeToParent[front] and nodeToParent[front] not in visited:
                    visited[nodeToParent[front]] = True
                    q.append(nodeToParent[front])
                    flag = True
            
            if flag == True:
                ans += 1

        return ans


    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        nodeToParent = {}
        targetNode = self.createParentMapping(root,start,nodeToParent)
        ans = self.infectTree(root, targetNode, nodeToParent)
        return ans