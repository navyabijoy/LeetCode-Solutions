class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        v = len(isConnected)
        adjLs = [[] for _ in range(v)]  # Create an adjacency list with empty lists        v = len(isConnected)
        # create an adjacency list
        for i in range(v):
            for j in range(v):
                if isConnected[i][j] == 1 and i != j:
                    adjLs[i].append(j)
                    adjLs[j].append(i)
        
        #create a dfs/bfs function
        def dfs(node, adjLs, visited):
            visited[node] = True
            for neighbor in adjLs[node]:
                if not visited[neighbor]:
                    dfs(neighbor, adjLs, visited)

        visited = [False] * v
        count = 0
        for i in range(v):
            if visited[i] is False:
                count += 1
                dfs(i, adjLs, visited)

        return count
