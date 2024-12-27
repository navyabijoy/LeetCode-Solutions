class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # better solution
        rows = [0] * len(matrix)
        cols = [0] * len(matrix[0])
        for r in range (len(rows)):
            for c in range(len(cols)):
                if matrix[r][c] == 0:
                    rows[r] = 1
                    cols[c] = 1

        for r in range (len(rows)):
            for c in range(len(cols)):
                if rows[r] == 1 or cols[c]==1:
                    matrix[r][c] = 0


        return matrix
        