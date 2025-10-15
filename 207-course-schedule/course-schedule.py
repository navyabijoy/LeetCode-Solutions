class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        in_degree = [0] * n
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[u].append(v)
            in_degree[v] += 1

        q = deque()

        for i in range(n):
            if in_degree[i] == 0:
                q.append(i)
        
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for nei in adj[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
        
        if len(topo) != n:
            return False
        else:
            return True
