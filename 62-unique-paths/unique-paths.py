class Solution:
    def helper(self,i,j,dp):
        if i == 0 and j == 0:
            return 1 # we have reached the top grid
        if i < 0 or j < 0:
            return 0 # out of bounds
        # step 3: check if the value is already stored
        if dp[i][j] != -1:
            return dp[i][j]
        # we start from the right most corner and then proceed to subtract 
        up = self.helper(i-1,j,dp)
        left = self.helper(i,j-1,dp) 
        dp[i][j] = up + left # step 2: store the value
        return dp[i][j]


    def uniquePaths(self, m: int, n: int) -> int:
        # step 1: define the dp array
        dp = [[-1]*n for _ in range(m)]
        return self.helper(m-1,n-1,dp)