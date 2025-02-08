class Solution:
    # top down approach + memoization
    def helper(self,cost, n,dp):

        if n == 0: # at the 0th step
            return cost[0]
        if n == 1: # at the first step
            return cost[1]
        if dp[n] != -1:
            return dp[n]
        # adds the cost of the current step, then chooses the step
        # where the step cost is minimum
        dp[n] = cost[n] + min(self.helper(cost,n-1,dp),self.helper(cost,n-2,dp))
        return dp[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * (n+1) # step 2
        ans = min(self.helper(cost, n-1,dp),self.helper(cost,n-2,dp))
        return ans