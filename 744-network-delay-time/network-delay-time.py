class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,wt in times:
            adj[u].append((v,wt))
        
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        
        heap = [(0,k)]

        while heap:

            time,node = heapq.heappop(heap)
            
            for nei, wt in adj[node]:
                new_time = time + wt

                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(heap,(new_time, nei))
        
        max_time = max(dist[1:])
        return max_time if max_time != float('inf') else -1

