class Solution:
    # bottom up approach -> tabulation
    def helper(self,cost, n):

        prev2 = cost[0] # step 2: analyze base case, add initial values
        prev1 = cost[1]
        
        # adds the cost of the current step, then chooses the step
        # where the step cost is minimum
        for i in range(2,n):
            curr = cost[i] + min(prev1,prev2)
            prev2 = prev1
            prev1 = curr
        return min(prev1,prev2)

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        return self.helper(cost,n)