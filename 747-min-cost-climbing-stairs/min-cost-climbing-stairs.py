class Solution:
    # bottom up approach -> tabulation
    def helper(self,cost, n,dp):

        dp[0] = cost[0]
        dp[1] = cost[1]
        
        # adds the cost of the current step, then chooses the step
        # where the step cost is minimum
        for i in range(2,n+1):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])
        return dp[n]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * (n+1) # step 2
        ans = min(self.helper(cost, n-1,dp),self.helper(cost,n-2,dp))
        return ans