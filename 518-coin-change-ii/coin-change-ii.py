class Solution:
    def solve(self, amt, coins, idx,dp):
        if amt == 0: # success case
            # “How many ways can I make amount 0?” → exactly 1 way, which is by choosing no more coins
            return 1

        if idx == len(coins): 
            # ive run out of coins, how many ways can i change the amount? 0
            return 0
        
        if (amt,idx) in dp:
            return dp[(amt,idx)]

        incl = self.solve(amt - coins[idx], coins, idx,dp) if amt - coins[idx] >= 0 else 0
        excl = self.solve(amt, coins, idx + 1,dp)

        dp[(amt,idx)] = incl + excl
        return dp[(amt,idx)]

    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        ans = self.solve(amount, coins, 0,dp)
        return ans 
