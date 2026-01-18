class Solution:
    def isValid(self, grid, row, col, i, j, size):
        target = row[i][j + size] - row[i][j]
        for s in range(size):
            if (row[i + s][j + size] - row[i + s][j]) != target:
                return False
        for s in range(size):
            if (col[i + size][j + s] - col[i][j + s]) != target:
                return False
        d1 = d2 = 0
        for k in range(size):
            d1 += grid[i + k][j + k]
            d2 += grid[i + size - 1 - k][j + k]
        return d1 == target and d2 == target

    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = [[0] * (n + 1) for _ in range(m)]
        col = [[0] * n for _ in range(m + 1)]

        # prefix sum of row
        for i in range(m):
            for j in range(n):
                row[i][j + 1] = row[i][j] + grid[i][j]

        # prefix sum of col
        for j in range(n):
            for i in range(m):
                col[i + 1][j] = col[i][j] + grid[i][j]

        ans = 1
        for i in range(m):
            for j in range(n):
                for size in range(min(m - i, n - j), ans, -1):
                    if self.isValid(grid, row, col, i, j, size):
                        ans = size
                        break
        return ans
