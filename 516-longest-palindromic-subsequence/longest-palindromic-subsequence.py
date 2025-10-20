class Solution:
    def solve(self, text1, text2):
        n = len(text1)
        dp = [[0] * (n+1) for _ in range(n+1)]

        
        for i in range(len(text1)):
            for j in range(len(text2)):
                ans = 0
                if text1[i] == text2[j]:
                    ans = 1 + dp[i - 1][j - 1]
                else:
                    ans = max(
                        dp[i - 1][j],
                        dp[i][j - 1],
                    )

                dp[i][j] = ans

        return dp[n - 1][n - 1]

    def longestPalindromeSubseq(self, s: str) -> int:
        revs = s[::-1]

        return self.solve(s, revs)
