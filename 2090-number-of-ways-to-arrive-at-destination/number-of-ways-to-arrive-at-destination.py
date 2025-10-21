MOD = 10**9 + 7
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u,v,t in roads:
            adj[u].append((v,t))
            adj[v].append((u,t))
        
        heap = [(0,0)]
        dist = [float('inf')] * (n)
        dist[0] = 0
        ways = [0] * n
        ways[0] = 1
        while heap:
            time, node = heapq.heappop(heap)
            if time > dist[node]:
                continue
            for nei, wt in adj[node]:
                new_time = time + wt
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    ways[nei] = ways[node]
                    heapq.heappush(heap, (new_time, nei))
                elif new_time == dist[nei]:
                    ways[nei] = (ways[nei] + ways[node]) % MOD

        # min_time = min(ways)
        # count = 0
        # for t in ways:
        #     if t == min_time:
        #         count += 0
        return ways[n-1] % MOD
    
