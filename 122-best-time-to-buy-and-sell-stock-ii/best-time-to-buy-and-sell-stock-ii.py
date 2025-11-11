class Solution:
    def calculate_profit(self, prices):
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+1)]

        dp[n][0] = 0
        dp[n][1] = 0
        for i in range(n-1,-1,-1):
            for j in range(2):
                profit = 0
                if j == 1:
                    buy_share = -prices[i] + dp[i + 1][0]
                    not_buy = 0 + dp[i+1][1]
                    profit = max(buy_share, not_buy)

                else:  # we can not buy , as we are supposed to sell now
                    sell_share = prices[i] + dp[i+1][1]
                    not_sell = 0 + dp[i+1][0]
                    profit = max(sell_share, not_sell)
                dp[i][j] = profit
        return dp[0][1]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        ans = self.calculate_profit(prices)
        return ans
