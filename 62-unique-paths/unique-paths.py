class Solution:
    def solve(self,m,n):
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        
        direction = [[-1,0],[0,-1]] # the path can only be top, left
        

        for i in range(m):
            for j in range(n):
                
                if i == 0 and j == 0:
                    continue # already set the value
                path = 0
                for r,c in direction:
                    new_r = i + r
                    new_c = j + c
                    if 0 <= new_r < m and 0 <= new_c < n:
                        path += dp[new_r][new_c]
                dp[i][j] = path

        return dp[m-1][n-1] 

    def uniquePaths(self, m: int, n: int) -> int:
        
        ans = self.solve(m,n)
        return ans
        