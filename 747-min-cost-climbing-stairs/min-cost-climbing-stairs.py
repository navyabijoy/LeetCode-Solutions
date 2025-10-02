class Solution:
    def solve(self,cost,n):
        # step 1: create dp array
        dp = [-1] * (n+1)

        # step 2: convert base case to store dp
        dp[0] = cost[0]
        
        dp[1] = cost[1]
        
        # step 3: convert to for loop
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

        return min(dp[n-1], dp[n-2])

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        return self.solve(cost,n)