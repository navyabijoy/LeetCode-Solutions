class Solution:
    def solve(self,coins, amt):
        dp = [float('inf')] * (amt+1)

        dp[0] = 0

        for i in range(1, amt+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
        
        
        return dp[amt] if dp[amt] != float('inf') else -1
 
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = self.solve(coins,amount)

        return ans