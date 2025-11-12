class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,wt in times:
            adj[u].append((v,wt))
        
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        heap = [(0,k)] # it shoes the 

        while heap:
            time, node = heapq.heappop(heap)
            for nei, t in adj[node]:
                if time + t >= dist[nei]:
                    continue
                dist[nei] = time+t
                heapq.heappush(heap, (time+t, nei))
        
        max_time = max(dist[1:])
        return max_time if max_time != float('inf') else -1

