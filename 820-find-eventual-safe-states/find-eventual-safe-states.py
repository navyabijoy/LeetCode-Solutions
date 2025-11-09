class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * (len(graph))
        for i in range(len(graph)):
            for g in graph[i]:
                adj[g].append(i)
                indegree[i] += 1
        q = deque()
        for i in range(len(graph)):
            if indegree[i] == 0:
                q.append(i) # indegree 0, terminal nodes
        
        topo =[]
        while q:
            node = q.popleft()
            topo.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return sorted(topo)
        
