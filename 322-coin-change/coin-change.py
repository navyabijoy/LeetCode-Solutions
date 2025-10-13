class Solution:
    def solve(self, coins, amt):
        n = len(coins)
        dp = [[float("inf")] * (amt + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0
        # for: if amt == 0:
        #         return 0

        for i in range(n - 1, -1, -1):
            for j in range(1, amt + 1):
                take = float("inf")
                if j - coins[i] >= 0:
                    take = 1 + dp[i][j - coins[i]]
                not_take = dp[i + 1][j]
                dp[i][j] = min(take, not_take)

        return dp[0][amt]

    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = self.solve(coins, amount)
        return ans if ans != float("inf") else -1
