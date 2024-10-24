class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True 

        #dfs with stack
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()#keep track of visited nodes
        seen.add(source)
        stack = [source]

        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for nei_node in graph[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    stack.append(nei_node)
        return False