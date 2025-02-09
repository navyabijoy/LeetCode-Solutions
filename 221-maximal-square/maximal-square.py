from typing import List

class Solution:
    def helper(self, mat, maxi):
        rows = len(mat)
        cols = len(mat[0])
        
        # Convert the matrix from strings to integers
        for i in range(rows):
            for j in range(cols):
                mat[i][j] = int(mat[i][j])
                maxi[0] = max(maxi[0],mat[i][j])

        for i in range(1, rows):  # Start from row 1
            for j in range(1, cols):  # Start from column 1
                if mat[i][j] == 1:
                    mat[i][j] = 1 + min(mat[i-1][j], mat[i][j-1], mat[i-1][j-1])
                maxi[0] = max(maxi[0], mat[i][j])  # Update maximum square size
        
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        maxi = [0] 
        
        self.helper(matrix, maxi)

        return maxi[0] ** 2
