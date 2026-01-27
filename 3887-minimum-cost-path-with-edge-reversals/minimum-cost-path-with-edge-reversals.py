class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        rev_adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            rev_adj[v].append((u, w))
        
        dist = [float('inf')] * n
        dist[0] = 0

        heap = [(0, 0)]
        while heap:
            node_dist, node = heapq.heappop(heap)
            if node_dist > dist[node]:
                continue
            
            for nei, weight in adj[node]:
                new_dist = node_dist + weight
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(heap, (new_dist, nei))
                
            for nei, weight in rev_adj[node]:
                rev_dist = node_dist + (2 * weight)
                if rev_dist < dist[nei]:
                    dist[nei] = rev_dist
                    heapq.heappush(heap, (rev_dist, nei))

        return dist[n-1] if dist[n-1] != float('inf') else -1