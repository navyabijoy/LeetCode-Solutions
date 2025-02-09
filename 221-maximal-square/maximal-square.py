class Solution:
    def helper(self,mat,maxi):
        rows = len(mat)
        cols = len(mat[0])
        dp = [[0] * cols for _ in range(rows)] # step 1:created a 2D DP array
        for i in range(rows):
            for j in range(cols):
                right = dp[i-1][j]
                diag = dp[i-1][j-1]
                down = dp[i][j-1]

                if mat[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1+ min(right,diag,down)
                else:
                    dp[i][j] = 0
                maxi[0] = max(maxi[0],dp[i][j])

        return dp[0][0] 

        # # base case, if r and c exceed rows and cols value
        # if r >= rows or c >= cols:
        #     return 0

        # if dp[r][c] != -1: # step 3: check if its occupied
        #     return dp[r][c]
        
        
        # if mat[r][c] == '1':
        #     dp[r][c] = 1 + min(right,diag,down) # step 2: store the values
        #     maxi[0] = max(maxi[0],dp[r][c])
        # else:
        #     dp[r][c] = 0
        # return dp[r][c]

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        # rows = len(matrix)
        # cols = len(matrix[0])

        maxi = [0] 
        self.helper(matrix, maxi)
        return maxi[0] ** 2 