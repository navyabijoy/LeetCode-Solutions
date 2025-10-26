class DisjointSet:
    def __init__(self, n):
        self.size = [1] * (n+1)
        self.parent = [i for i in range(n+1)]

    def findUParent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.findUParent(self.parent[node])
        return self.parent[node]

    def unionBySize(self,u,v):
        ulp_u = self.findUParent(u)
        ulp_v = self.findUParent(v)
        if ulp_u == ulp_v:
            return
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        maxRow = max(stone[0] for stone in stones)
        maxCol = max(stone[1] for stone in stones)
        ds = DisjointSet(maxRow + maxCol + 1)

        stoneNode = set()
        for r, c in stones:
            rowNode = r
            colNode = c + maxRow + 1
            ds.unionBySize(rowNode, colNode)
            stoneNode.add(rowNode)
            stoneNode.add(colNode)

        countComp = 0
        for node in stoneNode:
            if ds.findUParent(node) == node:
                countComp += 1

        return len(stones) - countComp
