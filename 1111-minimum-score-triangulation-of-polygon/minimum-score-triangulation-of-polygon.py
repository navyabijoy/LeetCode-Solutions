class Solution:
    def solve(self,vertex):
        n = len(vertex)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i+2, n):

                ans = float('inf')
                for k in range(i+1,j):
                    ans = min(ans, (vertex[i]*vertex[k]*vertex[j]) + dp[i][k] + dp[k][j])
                
                dp[i][j] = ans
        return dp[0][n-1]


    def minScoreTriangulation(self, values: List[int]) -> int:
        
        
        ans = self.solve(values)
        return ans