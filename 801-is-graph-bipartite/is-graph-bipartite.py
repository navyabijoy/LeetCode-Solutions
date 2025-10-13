class Solution:
    def dfs(self,graph, colors, node, color):
        if colors[node] != 0: # matlab that node is colored
            return colors[node] == color

        colors[node] = color

        for nei in graph[node]:
            if not self.dfs(graph, colors, nei, -color):
                return False

        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        v = len(graph)
        color = [0] * v

        for i in range(v):
            if color[i] == 0: # not colored
                if not self.dfs(graph, color, i , 1):
                    return False

        return True