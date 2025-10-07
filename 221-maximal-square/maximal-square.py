class Solution:
    def helper(self,mat,r,c,maxi):
        rows = len(mat)
        cols = len(mat[0])
        dp = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                right = dp[i-1][j]
                diag = dp[i-1][j-1]
                down = dp[i][j-1]

                if mat[i][j] == '1':
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(right,diag,down) # step 2: store the values
                else:
                    dp[i][j] = 0
                maxi[0] = max(maxi[0], dp[i][j])
        return dp[0][0] 

    def maximalSquare(self, matrix) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

         # step 1:created a 2D DP array
        maxi = [0] 
        self.helper(matrix, 0, 0, maxi)
        return maxi[0] ** 2 