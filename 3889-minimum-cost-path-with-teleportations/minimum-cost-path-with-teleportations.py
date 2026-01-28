class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[float('inf')] * n for _ in range(m)] for _ in range(k + 1)]
        dp[0][0][0] = 0

        # Pre-collect all grid values and sort them to use for prefix mins
        all_values = sorted(list(set(val for row in grid for val in row)), reverse=True)
        val_to_idx = {val: i for i, val in enumerate(all_values)}

        for p in range(k + 1):
            # 1. Normal Moves (Down/Right)
            for r in range(m):
                for c in range(n):
                    if dp[p][r][c] == float('inf'): continue
                    if r + 1 < m:
                        dp[p][r+1][c] = min(dp[p][r+1][c], dp[p][r][c] + grid[r+1][c])
                    if c + 1 < n:
                        dp[p][r][c+1] = min(dp[p][r][c+1], dp[p][r][c] + grid[r][c+1])

            # 2. Optimized Teleportation to p + 1
            if p < k:
                # Find the best entry cost in layer p for each starting grid value
                # We want: best_cost_for_val[v] = min(dp[p][r][c]) where grid[r][c] == v
                best_at_val = [float('inf')] * len(all_values)
                for r in range(m):
                    for c in range(n):
                        if dp[p][r][c] != float('inf'):
                            idx = val_to_idx[grid[r][c]]
                            best_at_val[idx] = min(best_at_val[idx], dp[p][r][c])
                
                # Prefix Minimum: best_at_val[i] will now store min cost 
                # for any cell with value >= all_values[i]
                for i in range(1, len(all_values)):
                    best_at_val[i] = min(best_at_val[i], best_at_val[i-1])
                
                # Now, for every destination cell in p+1, the jump cost is 
                # the best cost from any cell in p with grid[r][c] >= grid[nr][nc]
                for nr in range(m):
                    for nc in range(n):
                        idx = val_to_idx[grid[nr][nc]]
                        dp[p+1][nr][nc] = min(dp[p+1][nr][nc], best_at_val[idx])

        ans = min(dp[layer][m-1][n-1] for layer in range(k + 1))
        return ans if ans != float('inf') else -1
