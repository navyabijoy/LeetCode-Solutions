# Last updated: 5/22/2025, 12:17:06 AM
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # better solution
        rows = [0] * len(matrix) #O(m)
        cols = [0] * len(matrix[0]) #O(n)
        for r in range (len(rows)):
            for c in range(len(cols)): #O(m*n)
                if matrix[r][c] == 0:
                    rows[r] = 1
                    cols[c] = 1

        for r in range (len(rows)):
            for c in range(len(cols)): # + O(m*n)
                if rows[r] == 1 or cols[c]==1:
                    matrix[r][c] = 0

        #space: O(m) + O(n)
        #time: O(2*m*n)
        return matrix
        