class Solution:
    def solve(self, coins, idx, amt):
        dp = [[0] * (amt + 1) for _ in range(len(coins)+1)]
        prev = [0] * (amt+1)
        curr = [0] * (amt+1)
        
        prev[0] = 1

        for i in range(len(coins)-1,-1,-1):
            curr[0] = 1
            for j in range(1,amt+1):                    
                incl = 0
                if j - coins[i] >= 0:
                    incl = curr[j - coins[i]]
                excl = prev[j] 

                curr[j] = incl + excl
            prev = curr[:]

        return prev[amt]

    def change(self, amount: int, coins: List[int]) -> int:
        
        ans = self.solve(coins,0,amount)
        return ans 
