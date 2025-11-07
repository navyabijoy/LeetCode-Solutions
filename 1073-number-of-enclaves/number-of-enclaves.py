class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        vis = [[False] * n for _ in range(m)]
        mat = [[0] * n for _ in range(m)]
        for i in range(m):
            if not vis[i][0] and grid[i][0] == 1:
                q.append([i,0])

            if not vis[i][n-1] and grid[i][n-1] == 1:
                q.append([i,n-1])

        for i in range(n):
            if not vis[0][i] and grid[0][i] == 1:
                q.append([0,i])

            if not vis[m-1][i] and grid[m-1][i] == 1:
                q.append([m-1,i])
       
        # all the corner 1s have been added in the queue
        distance = [ (0,1), (0,-1), (1,0), (-1,0)]
        count = 0
        while q:
            row, col = q.popleft()
            vis[row][col] = True
            grid[row][col] = 2
            for dr, dc in distance:
                nrow = dr + row
                ncol = dc + col
                if 0 <= nrow < m and 0 <= ncol < n and not vis[nrow][ncol] and grid[nrow][ncol] == 1:
                    vis[nrow][ncol] = True
                    grid[nrow][ncol] = 2
                    q.append((nrow,ncol))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
        return count
