class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = defaultdict(list)
        vis = [False] * n
        count = 0
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    adj[i].append(j)
                    adj[j].append(i)
        for i in range(n):
            if vis[i] != True:
                count += 1
                self.dfs(i,adj,vis,isConnected, n,count)
        return count

    def dfs(self, node, adj, visited, mat, n, count):
        visited[node] = True
        for nei in adj[node]:
            if not visited[nei]:
                self.dfs(nei, adj, visited, mat, n, count)
