class Solution:
    def helper(self,mat,r,c,maxi,dp):
        rows = len(mat)
        cols = len(mat[0])

        # base case, if r and c exceed rows and cols value
        if r >= rows or c >= cols:
            return 0

        if dp[r][c] != -1: # step 3: check if its occupied
            return dp[r][c]
        
        right = self.helper(mat,r,c+1,maxi,dp)
        diag = self.helper(mat,r+1,c+1,maxi,dp)
        down = self.helper(mat,r+1,c,maxi,dp)

        if mat[r][c] == '1':
            dp[r][c] = 1 + min(right,diag,down) # step 2: store the values
            maxi[0] = max(maxi[0],dp[r][c])
        else:
            dp[r][c] = 0
        return dp[r][c]

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[-1] * cols for _ in range(rows)] # step 1:created a 2D DP array
        maxi = [0] 
        self.helper(matrix, 0, 0, maxi,dp)
        return maxi[0] ** 2 