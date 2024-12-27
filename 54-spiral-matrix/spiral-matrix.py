class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0:
            return res
        row_begin = 0
        col_begin = 0
        row_end = len(matrix)-1 
        col_end = len(matrix[0])-1
        while (row_begin <= row_end and col_begin <= col_end):
            # goes from left -> right in the same row
            for i in range(col_begin,col_end+1):
                res.append(matrix[row_begin][i]) #the row is static
            row_begin += 1 #row moves down

            # goes from top -> bottom in the same col
            
            for i in range(row_begin,row_end+1):
                res.append(matrix[i][col_end]) #the column is static
            col_end -= 1 #column comes to the left

            # goes from right -> left in the same row
            if (row_begin <= row_end):

                for i in range(col_end,col_begin-1,-1):
                    res.append(matrix[row_end][i]) #row is static
                row_end -= 1 #move the row end upwards

            # goes from bottom -> top in the same col
            if (col_begin <= col_end):
                for i in range(row_end,row_begin-1,-1):
                    res.append(matrix[i][col_begin]) #col is static
                col_begin += 1 #move the column towards right

        return res
