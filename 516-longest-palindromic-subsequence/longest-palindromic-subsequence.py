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
                self.solve(text1, text2, i - 1, j, dp),
                self.solve(text1, text2, i, j - 1, dp),
            )

        dp[i][j] = ans
        return dp[i][j]

    def longestPalindromeSubseq(self, s: str) -> int:
        revs = s[::-1]
        n = len(s)
        dp = [[-1] * n for _ in range(n)]
        return self.solve(s, revs, n - 1, n - 1, dp)
