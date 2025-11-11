class Solution:
    def calculate_profit(self, prices):
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+2)]

        for i in range(n-1,-1,-1):
            for j in range(2):
                profit = 0
                if j == 1:
                    buy_share = -prices[i] + dp[i+ 1][0]
                    skip_share = 0 + dp[i+ 1][1]
                    profit = max(buy_share, skip_share)
                else:
                    sell_share = +prices[i] + dp[i + 2][1]
                    skip_share = 0 + dp[i+1][0]
                    profit = max(sell_share, skip_share)
                dp[i][j] = profit
        return dp[0][1]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = self.calculate_profit(prices)
        return ans
