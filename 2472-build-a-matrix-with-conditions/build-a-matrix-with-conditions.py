class Solution:
    def topoSort(self, edges, V):
        adj = defaultdict(list)
        indegree = [0] * (V+1)
        for u,v in edges:
            adj[u].append(v)
            indegree[v] += 1
        
        q = deque()
        for i in range(1, V+1):
            if indegree[i] == 0:
                q.append(i)
        
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return topo

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        matrix = [[0] * k for _ in range(k)]
        rows = self.topoSort(rowConditions, k)
        cols = self.topoSort(colConditions, k)

        # there might be no topological order itself
        if len(rows) < k or len(cols) < k:
            return []
        
        row_map = {num: i for i, num in enumerate(rows)}
        col_map = {num: i for i, num in enumerate(cols)}

        for num in range(1, k+1):
            r = row_map[num]
            c = col_map[num]
            matrix[r][c] = num
        return matrix
