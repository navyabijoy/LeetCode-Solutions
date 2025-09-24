class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # step 1. Adjacency list
        adj = defaultdict(list)
        
        for u,v,w in times:
            adj[u].append((v,w))
            

        # step 2. create the shortest distance array
        dist = [float('inf')] * (n+1)

        # set the distance from source node to 0
        dist[k] = 0

        # step 3. create min heap (distance, node)
        heap = [(0, k)]

        while heap:
            node_dist, node = heapq.heappop(heap)
            
            # skip if we already have a better distance
            if node_dist > dist[node]:
                continue

            for nei, weight in adj[node]:
                new_dist = node_dist + weight
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(heap, [new_dist, nei])
        
        max_dist = max(dist[1:])

        return max_dist if max_dist != float('inf') else -1