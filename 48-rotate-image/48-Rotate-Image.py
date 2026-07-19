class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # step 1 : transpose (converts rows -> cols)
        
        m, n = len(matrix[0]), len(matrix)
        for i in range(m):
            for j in range(i, n): # first triangle
                matrix[i][j], matrix[j][i] =  matrix[j][i],  matrix[i][j]
                # swap values to change in place
        
        # step 2 : reverse rows
        for row in matrix:
            row.reverse()
            # start = 0
            # end = n - 1
            # while start < end:
            #     row[start], row[end] = row[end], row[start]
            #     start += 1
            #     end -= 1
            
        