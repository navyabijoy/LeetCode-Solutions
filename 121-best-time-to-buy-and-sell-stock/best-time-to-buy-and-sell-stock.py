class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for price in prices:
            diff = price - buy
            profit = max(profit, diff)
            buy = min(buy, price)
        return profit