class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        vis = [[0] * n for _ in range(m)]
        dis = [[0] * n for _ in range(m)]

        q = deque()
        
        # append all cells with 0 in the queue
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append(((i,j),0))
                    vis[i][j] = 1
                else:
                    vis[i][j] = 0
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while q:
            (row,col), step = q.popleft()
            dis[row][col] = step 
            # check all 4 directions with step count as same
            for dr, dc in directions:
                nrow = row + dr
                ncol = col + dc

                if 0 <= nrow < m and 0 <= ncol < n and not vis[nrow][ncol]:
                    vis[nrow][ncol] = 1
                    q.append(((nrow,ncol), step + 1))
        
        return dis