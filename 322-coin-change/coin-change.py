class Solution:
    def helper(self,coins,amt,dp):
        if amt == 0: # base case - amount has become 0 after all the needed subtraction
            return 0
        if amt < 0: # when it was subtracted more than needed of number were huge
            return float('inf')
        if dp[amt]!= -1:
            return dp[amt]

        mini = float('inf')
        
        for coin in coins:
            # subtract the value of the current coin from the target
            ans = self.helper(coins, amt-coin,dp) 
            if ans != float('inf'):
                mini = min(mini, ans+1) 
        dp[amt] = mini
        return mini

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount+1)
        ans = self.helper(coins,amount,dp)
        if ans == float('inf'):
            return -1
        return ans