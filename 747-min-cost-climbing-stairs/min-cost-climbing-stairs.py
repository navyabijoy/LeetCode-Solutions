class Solution:
    # bottom up approach -> tabulation
    def helper(self,cost, n):
        dp = [-1] * (n+1) # step 1: creation

        dp[0] = cost[0] # step 2: analyze base case, add initial values
        dp[1] = cost[1]
        
        # adds the cost of the current step, then chooses the step
        # where the step cost is minimum
        for i in range(2,n):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])
        return min(dp[n-1],dp[n-2])

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        return self.helper(cost,n)