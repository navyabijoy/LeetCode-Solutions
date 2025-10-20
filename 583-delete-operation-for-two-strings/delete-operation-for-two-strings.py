class Solution:
    def solve(self, text1, text2, i, j, dp):
        if i < 0 or j < 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        ans = 0
        if text1[i] == text2[j]:
            ans = 1 + self.solve(text1, text2, i - 1, j - 1, dp)
        else:
            ans = max(
                self.solve(text1, text2, i, j - 1, dp),
                self.solve(text1, text2, i - 1, j, dp),
            )

        dp[i][j] = ans
        return dp[i][j]

    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[-1] * n for _ in range(m)]
        ans = self.solve(word1, word2, m - 1, n - 1, dp)
        return (m - ans) + (n - ans)
