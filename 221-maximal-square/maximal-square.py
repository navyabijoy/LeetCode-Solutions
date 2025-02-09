class Solution:
    def helper(self,mat,maxi):
        rows = len(mat)
        cols = len(mat[0])
        # convert the string array to int
        for r in range(rows):
            for c in range(cols):
                mat[r][c] = int(mat[r][c])
                maxi[0] = max(maxi[0],mat[r][c])

        for i in range(1,rows): # start from row 1
            for j in range(1,cols): # start from column 1
                if mat[i][j] == 1: 
                    mat[i][j] = 1 + min(mat[i-1][j], mat[i][j-1], mat[i-1][j-1])
                maxi[0] = max(maxi[0], mat[i][j])
        # return maxi[0] 


    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        maxi = [0] 
        self.helper(matrix, maxi)
        return maxi[0] ** 2 