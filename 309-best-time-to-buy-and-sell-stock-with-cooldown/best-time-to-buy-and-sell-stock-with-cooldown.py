class Solution:
    def calculate_profit(self, prices):
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+2)]
        
        next1_dp = [0,0]
        next2_dp = [0,0]
        curr_dp = [0, 0]
        for i in range(n-1,-1,-1):
            for j in range(2):
                profit = 0
                if j == 1:
                    buy_share = -prices[i] + next1_dp[0]
                    skip_share = 0 + next1_dp[1]
                    profit = max(buy_share, skip_share)
                else:
                    sell_share = +prices[i] + next2_dp[1]
                    skip_share = 0 + next1_dp[0]
                    profit = max(sell_share, skip_share)
                curr_dp[j] = profit
            next2_dp = next1_dp[:]
            next1_dp = curr_dp[:]
        return next1_dp[1]

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = self.calculate_profit(prices)
        return ans
