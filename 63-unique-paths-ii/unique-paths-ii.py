class Solution:
    def helper(self,mat,i,j):
        # if the starting cell has an obstacle
        if mat[0][0] == 1:
            return 0
        curr = [0] * j
        prev = [0] * j
        for r in range(i):
            for c in range(j):
                if mat[r][c] == 1:
                    curr[c] = 0
                    continue
                if r == 0 and c == 0:
                    curr[0] = 1
                    continue
                up = prev[c] if r > 0 else 0
                left = curr[c-1] if c> 0 else 0
                curr[c] = up +left
            prev = curr[:]
    
        return prev[j-1]
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        ans = self.helper(obstacleGrid,row,col)
        return ans