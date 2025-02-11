class Solution:
    def helper(self,grid,m,n,dp):
        if m == 0 and n == 0:
            return grid[0][0]
        if m < 0 or n < 0:
            return float('inf')
        if dp[m][n] != -1:
            return dp[m][n]


        up=grid[m][n] + self.helper(grid,m-1,n,dp)
        left=grid[m][n] + self.helper(grid,m,n-1,dp)
        dp[m][n] = min(up,left)
        return dp[m][n]

    def minPathSum(self, grid: List[List[int]]) -> int:
        r, c = len(grid),len(grid[0])
        dp = [ [-1] * c for _ in range(r)]
        return self.helper(grid,r-1,c-1,dp)