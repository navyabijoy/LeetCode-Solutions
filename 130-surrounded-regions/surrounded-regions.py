class Solution:
    def dfs(self,row,col, vis,mat):
        vis[row][col] = 1 # mark the cell visited
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        m = len(mat)
        n = len(mat[0])
        for dr,dc in directions:
            nrow = row + dr
            ncol = col + dc
            if ( 0 <= nrow < m ) and 0 <= ncol < n and not vis[nrow][ncol] and mat[nrow][ncol] == 'O':
                self.dfs(nrow,ncol,vis,mat)

    def solve(self, mat: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(mat)
        n = len(mat[0])
        vis = [[0] * n for _ in range(m)]

        # first traverse to find the regions with 0 at the border

        # traverse first and last row
        for j in range(n):
            if not vis[0][j] and mat[0][j] == "O":
                self.dfs(0,j,vis,mat)
            if not vis[m-1][j] and mat[m-1][j] == "O":
                self.dfs(m-1,j,vis,mat)

        # traverse first and last col
        for i in range(m):
            if not vis[i][0] and mat[i][0] == 'O':
                self.dfs(i,0,vis,mat)
            if not vis[i][n-1] and mat[i][n-1] =='O':
                self.dfs(i,n-1,vis,mat)

        # convert unvisited 0 -> X
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and mat[i][j] == "O":
                    mat[i][j] = "X"
        
        return mat
            
        
        