class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for flight in flights:
            u,v,wt = flight
            adj[u].append((v,wt))
        
        q = deque()
        q.append([src,0])
        minCost = [float('inf')] * n
        stops = 0
        while q and stops <= k:
            level = len(q)
            for _ in range(level):
                node, cost = q.popleft()
                for nei, price in adj[node]:
                    if price + cost >= minCost[nei]:
                        continue
                    minCost[nei] = price + cost
                    q.append((nei, price+cost))
            stops += 1
        
        return -1 if minCost[dst] == float('inf') else minCost[dst] 