class Solution:
    def dfs(self,i,adj,vis):
        vis[i] = 1
        for nei in adj[i]:
            if vis[nei] == 0:
                self.dfs(nei,adj,vis)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        n = len(isConnected[0])
        adj = defaultdict(list)
        for r in range(m):
            for c in range(n):
                if isConnected[r][c] == 1 and r != c:
                    adj[r].append(c)
                    adj[c].append(r)
        
        vis = [0] * m
        count = 0
        for i in range(len(vis)):
            if vis[i] == 0:
                count += 1
                self.dfs(i, adj, vis)
        return count
            
