class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, -1
        direction = 1
        result = []

        while rows > 0 and cols > 0:

            for _ in range(cols):
                col += direction
                result.append(matrix[row][col]) #iterated the whole row
            rows -= 1 #decrease the row to iterate the row below it

            for _ in range(rows):
                row += direction
                result.append(matrix[row][col])
            cols -= 1
        
            direction *= -1
        return result
            

