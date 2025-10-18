class Solution:
    def solve(self, text1, text2, i,j,dp):
        if i == len(text1):
            return 0
        
        if j == len(text2):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        ans = 0
        if text1[i] == text2[j]:
            ans = 1 + self.solve(text1,text2,i+1,j+1,dp)
        else:
            ans = max(self.solve(text1,text2,i+1,j,dp), self.solve(text1,text2,i,j+1,dp))
        
        dp[i][j] = ans
        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1] * (len(text2)) for _ in range((len(text1)))]
        return self.solve(text1,text2,0,0,dp)