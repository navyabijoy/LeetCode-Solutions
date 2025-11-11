class Solution:
    def calculate_profit(self, index, prices, buy, dp):
        if index >= len(prices):
            return 0
        if dp[index][buy] != -1:
            return dp[index][buy]
        profit = 0
        if buy:
            buy_share = -prices[index] + self.calculate_profit(index + 1, prices, False,dp)
            skip_share = 0 + self.calculate_profit(index + 1, prices, True, dp)
            profit = max(buy_share, skip_share)
        else:
            sell_share = +prices[index] + self.calculate_profit(index + 2, prices, True, dp)
            skip_share = 0 + self.calculate_profit(index + 1, prices, False, dp)
            profit = max(sell_share, skip_share)
        dp[index][buy] = profit
        return dp[index][buy]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]
        ans = self.calculate_profit(0, prices, True, dp)
        return ans
