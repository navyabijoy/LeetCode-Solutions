class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid) #rows
        m = len(grid[0]) #column
        visited = [[False] * m for _ in range(n)]
        count = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == '1' and not visited[row][col]:
                    count += 1
                    self.bfs(row, col, visited, grid)
        return count

    def bfs(self, row:int, col:int, visited: List[List[bool]], grid: List[List[str]]):
        queue = deque([(row, col)])
        visited[row][col] = True
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        while queue:
            curr_row, curr_col = queue.popleft()
            for dr,dc in directions:
                new_row, new_col = curr_row + dr, curr_col + dc
                if ( 0<= new_row < len(grid) and 0 <= new_col < len(grid[0]) and
                grid[new_row][new_col] == '1' and not visited[new_row][new_col]):
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col))
