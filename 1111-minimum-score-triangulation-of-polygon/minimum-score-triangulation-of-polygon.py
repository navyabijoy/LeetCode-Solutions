class Solution:
    def solve(self,vertex,i,j,dp):
        if i+1 == j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]

        ans = float('inf')
        for k in range(i+1,j):
            ans = min(ans, (vertex[i]*vertex[k]*vertex[j]) + self.solve(vertex,i,k,dp) + self.solve(vertex,k,j,dp))
        
        dp[i][j] = ans
        return dp[i][j]


    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        ans = self.solve(values, 0, n-1,dp)
        return ans