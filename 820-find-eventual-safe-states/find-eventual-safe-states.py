class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = defaultdict(list)
        outdegree = [0] * n
        for i in range(len(graph)):
            for nei in graph[i]:
                adj[nei].append(i)   # reverse the edge
            outdegree[i] = len(graph[i])
                
        topo = []
        q = deque()

        for i in range(n):
            if outdegree[i] == 0:
                q.append(i) # we have terminal nodes now
        
        while q:
            node = q.popleft()
            topo.append(node)
            for nei in adj[node]:
                outdegree[nei] -= 1
                if outdegree[nei] == 0:
                    q.append(nei)
        return sorted(topo)