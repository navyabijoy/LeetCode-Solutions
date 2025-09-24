class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj =  defaultdict(list)

        for u,v,w in times:
            adj[u].append((v,w))

        dist = [(float('inf'))] * (n+1)
        dist[k] = 0

        heap = [(0,k)] # [(distance, node)]

        while heap:
            node_distance, node = heapq.heappop(heap)

            if node_distance > dist[node]:
                continue

            for nei, weight in adj[node]:
                new_dist = node_distance + weight
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(heap, (new_dist, nei))
        
        max_dist = max(dist[1:])
        return max_dist if max_dist != float('inf') else -1

