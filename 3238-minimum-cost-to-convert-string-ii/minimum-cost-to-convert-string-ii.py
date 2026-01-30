class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        n = len(source)

        # Build Index {substring -> i}
        index = dict()
        for s in original + changed:
            if s not in index:
                index[s] = len(index)
        K = len(index)

        # Create Distances
        dist = [[math.inf] * K for _ in range(K)]
        for o, c, w in zip(original, changed, cost):
            u, v = index[o], index[c]
            dist[u][v] = min(dist[u][v], w)

        # Floyd-Warshall for shortest paths
        for k in range(K):
            for u in range(K):
                if dist[u][k] != math.inf:  # Eliminate no path branch
                    for v in range(K):
                        if dist[k][v] != math.inf and dist[u][k] + dist[k][v] < dist[u][v]:
                            dist[u][v] = dist[u][k] + dist[k][v]

        lengths = set(map(len, original))

        # DP
        dp = [0] + [math.inf] * n
        for i in range(n):
            if dp[i] == math.inf:  # Skip if not reacheable
                continue

            if target[i] == source[i]:  # If chars match, try to update
                dp[i + 1] = min(dp[i + 1], dp[i])

            # For each position i we try to match all possible substring lengths
            for l in lengths:
                if i + l >= len(dp):
                    continue

                u = index.get(source[i: i + l], -1)
                v = index.get(target[i: i + l], -1)
                if u >= 0 and v >= 0:
                    dp[i + l] = min(dp[i + l], dp[i] + dist[u][v])

        return dp[-1] if dp[-1] != math.inf else -1