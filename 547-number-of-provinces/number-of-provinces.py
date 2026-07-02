class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        vis = [False] * n
        adj = defaultdict(list)
        count = 0 # to count the province
        for i in range(n): # [[1,1,0]
            for j in range(n): # [[1]
                if isConnected[i][j] == 1 and i != j:
                    adj[i].append(j)
                    adj[j].append(i) # to keep track of nodes connected to eo
        
        for i in range(n):
            if vis[i] == False:
                count += 1
                self.dfs(i, vis, adj)
        return count

    def dfs(self, node, vis, adj):
        vis[node] = True # mark the node visited since traversal is starting
        for nei in adj[node]:
            if not vis[nei]:
                self.dfs(nei, vis, adj)

                