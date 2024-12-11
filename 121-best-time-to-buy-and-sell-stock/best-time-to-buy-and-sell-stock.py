class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        mini,maxi = float('inf'),0
        for price in prices:
            mini = min(mini, price)

            profit = price - mini

            maxi = max(maxi, profit)
            
        return maxi