class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append([i,j]) # pushed all the rotten oranges
        time = 0
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        while q and fresh != 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    nrow = r + dr
                    ncol = c + dc
                    if 0 <= nrow < m and 0 <= ncol < n and grid[nrow][ncol] == 1:
                        grid[nrow][ncol] = 2
                        fresh -= 1
                        
                        q.append([nrow,ncol])
            time += 1

        return time if fresh == 0 else -1


        