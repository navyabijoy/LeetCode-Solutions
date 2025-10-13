class Solution:
    def solve(self,coins,idx,amt,dp):
        if amt == 0:
            return 0

        if amt < 0 or idx == len(coins):
            return float('inf') 
        
        if dp[idx][amt] != -1:
            return dp[idx][amt]

        take = 1 + self.solve(coins, idx, amt - coins[idx],dp)
        not_take = self.solve(coins,idx+1,amt,dp)

        dp[idx][amt] = min(take, not_take)
        return min(take, not_take)

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]
        ans = self.solve(coins,0,amount,dp)
        return ans if ans != float('inf') else -1
    
