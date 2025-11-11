class Solution:
    def calculate_profit(self, prices, index, buy, dp):
        if index == len(prices):
            return 0
        # if index == 0:
        #     return profit
        if dp[index][buy] != -1:
            return dp[index][buy]
        profit = 0
        if buy:
            buy_share = -prices[index] + self.calculate_profit(prices, index + 1, False, dp)
            not_buy = 0 + self.calculate_profit(prices, index + 1, True, dp)
            profit = max(buy_share, not_buy)

        else:  # we can not buy , as we are supposed to sell now
            sell_share = +prices[index] + self.calculate_profit(prices, index + 1, True, dp)
            not_sell = 0 + self.calculate_profit(prices, index + 1, False, dp)
            profit = max(sell_share, not_sell)
        dp[index][buy] = profit
        return dp[index][buy]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1] * 2 for _ in range(n)]
        ans = self.calculate_profit(prices, 0, True, dp)
        return ans
