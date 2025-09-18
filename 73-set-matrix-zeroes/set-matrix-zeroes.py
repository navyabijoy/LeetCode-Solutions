class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = len(matrix[0])
        row = len(matrix)
        rowZeroAt = []
        colZeroAt = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rowZeroAt.append(i)
                    colZeroAt.append(j)

        for i in range(row):
            for j in range(col):
                if i in rowZeroAt or j in colZeroAt:
                    matrix[i][j] = 0
        
        return matrix
