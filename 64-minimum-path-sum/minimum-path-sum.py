class Solution:
    def helper(self,mat,i,j):
        prev = [0] * j
        for r in range(i):
            curr = [0] * j
            for c in range(j):
                if r == 0 and c == 0:
                    curr[c] = mat[0][0]
                else:
                    up = mat[r][c] + prev[c] if r > 0 else float('inf')
                    left = mat[r][c] + curr[c-1] if c > 0 else float('inf')
                    curr[c] = min(up,left)
            prev=  curr
        return prev[-1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        return self.helper(grid,m,n)