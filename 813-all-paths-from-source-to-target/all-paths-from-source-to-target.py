class Solution:
    def dfs(self, graph, node, path, res, target):
        if node == target:
            res.append(list(path))
            return

        for neighbor in graph[node]:
            path.append(neighbor)
            self.dfs(graph,neighbor,path,res,target)
            path.pop() # backtrack

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        target = len(graph)-1
        self.dfs(graph,0,[0],res,target)
        return res
