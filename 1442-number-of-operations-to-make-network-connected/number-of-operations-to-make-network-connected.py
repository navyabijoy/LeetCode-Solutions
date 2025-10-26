class DisjointSet:
    def __init__(self, n):
        self.size = [1] * (n+1)
        self.parent = [i for i in range(n+1)]
    
    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUPar(self.parent[node]) # path compression -> finding the ultimate parent
        return self.parent[node]

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return 
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds = DisjointSet(n)
        countExtra = 0
        for u, v in connections:
            if ds.findUPar(u) == ds.findUPar(v):
                countExtra += 1
            else:
                ds.unionBySize(u,v)
        
        countComponents = 0
        for i in range(n):
            if ds.parent[i] == i:
                countComponents += 1

        ans = countComponents - 1
        if countExtra >= ans:
            return ans
        return -1