class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        if grid[0][0] != 0 or grid[m-1][n-1] != 0:
            return -1

        directions = [
                        (-1, 0),  # up
                        (1, 0),   # down
                        (0, -1),  # left
                        (0, 1),   # right
                        (-1, -1), # top-left
                        (-1, 1),  # top-right
                        (1, -1),  # bottom-left
                        (1, 1)    # bottom-right
                    ]
        vis = [[False]* n for _ in range(m)]
        vis[0][0] = True

        q = deque()
        q.append((0,0,1))
        while q:
            row,col, dist = q.popleft()

            if row == m-1 and col == n-1:
                return dist

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 0 and not vis[new_row][new_col]:
                    vis[new_row][new_col] = True
                    q.append((new_row, new_col, dist+1))
        
        return -1

