class Solution:
    def solve(self, mat):
        m = len(mat)
        dp = [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(m):
                if i == 0:
                    dp[0][j] = mat[0][j]
                else:
                    left_diag = float('inf')
                    right_diag = float('inf')
                    
                    up = mat[i][j] + dp[i-1][j]
                    if j - 1 >= 0:
                        left_diag = mat[i][j] + dp[i-1][j-1]
                    if j + 1 < m :
                        right_diag = mat[i][j] + dp[i-1][j+1]

                    dp[i][j] = min(up, left_diag, right_diag)

        return min(dp[m-1])


    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        return self.solve(matrix)
        