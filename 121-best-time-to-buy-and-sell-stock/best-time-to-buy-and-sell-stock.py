class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for p in prices:
            diff = p - buy
            profit = max(profit, diff)
            buy = min(buy, p)
        return profit
