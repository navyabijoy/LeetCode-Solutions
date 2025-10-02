class Solution:
    def solve(self,cost,n,dp):
        # step 1: base case 
        if n == 0:
            dp[0] = cost[0]
        if n == 1:
            dp[1] = cost[1]

        # step 2: after defining base case, check if the n value is present in dp array
        if dp[n] != -1:
            return dp[n]

        # step 3: store the value in dp array
        dp[n] = min(self.solve(cost, n-1,dp), self.solve(cost,n-2,dp)) + cost[n]
        return dp[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * n
        ans = min(self.solve(cost, n-1,dp), self.solve(cost, n-2,dp))
        return ans