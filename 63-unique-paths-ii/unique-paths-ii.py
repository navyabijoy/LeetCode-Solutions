class Solution:
    def solve(self,m,n,matrix,dp):
        if m < 0 or n < 0:
            return 0

        # when obstacle found, return 0
        if matrix[m][n] == 1:
            return 0

        if m == 0 and n == 0:
            return 1
        
        if dp[m][n] != -1:
            return dp[m][n]

        up = self.solve(m-1,n,matrix,dp)
        left = self.solve(m,n-1,matrix,dp)
        dp[m][n] = up+left
        return dp[m][n]
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        ans = self.solve(m-1,n-1,grid,dp)
        return ans