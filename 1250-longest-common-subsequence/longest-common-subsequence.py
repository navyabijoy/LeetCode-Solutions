class Solution:
    def solve(self, text1, text2, i,j,dp):
        if i == len(text1):
            return 0
        
        if j == len(text2):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        ans = 0
        res = ""
        if text1[i] == text2[j]:
            ans = 1 + self.solve(text1,text2,i+1,j+1,dp)
            res = text1[i+1]
        else:
            ans = max(self.solve(text1,text2,i+1,j,dp), self.solve(text1,text2,i,j+1,dp))
        
        dp[i][j] = ans
        return dp[i][j]

    def solveTab(self,text1,text2):
        dp = [[0] * (len(text2)+1) for _ in range((len(text1)+1))]
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                ans = 0
                if text1[i] == text2[j]:
                    ans = 1 + dp[i+1][j+1]
                else:
                    ans = max(dp[i+1][j], dp[i][j+1])
                
                dp[i][j] = ans
        return dp[0][0]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.solveTab(text1,text2)