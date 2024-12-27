class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = 1
        rows = len(matrix)
        cols = len(matrix[0])
        ans = []
        row, col = 0, -1

        while rows > 0 and cols > 0:
            for _ in range(cols):
                col += direction
                ans.append(matrix[row][col])
            rows -= 1

            for _ in range(rows):
                row += direction
                ans.append(matrix[row][col])
            cols -= 1

            direction *= -1
        return ans