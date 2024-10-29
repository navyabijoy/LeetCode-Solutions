class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid) #rows
        m = len(grid[0]) #column
        visited = [[False] * m for _ in range(n)] #creating a separate visited grid of the same dimension
        count = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == '1' and not visited[row][col]: #a new starting of the island is found
                    count += 1
                    self.bfs(row, col, visited, grid)
        return count

    def bfs(self, row:int, col:int, visited: List[List[bool]], grid: List[List[str]]):
        queue = deque([(row, col)]) #The queue will store cells to visit. We start by adding the initial cell (row, col) to the queue.
        visited[row][col] = True
        directions = [(0,1),(1,0),(0,-1),(-1,0)] #list of tuples representing the four possible moves
        #Each tuple is a direction: (0, 1) moves right, (1, 0) moves down, (0, -1) moves left, and (-1, 0) moves up.

        while queue:
            curr_row, curr_col = queue.popleft() #removes and returns the first element of the qeueue which is the cell
            #currently being explored
            for dr,dc in directions: #this loop iterates over each possible direction from the directions list
                #dr (delta row) and dc (delta column) are values to calculate the neighboring cell in each direction.
                new_row, new_col = curr_row + dr, curr_col + dc
                if ( 0<= new_row < len(grid) and 0 <= new_col < len(grid[0]) and
                grid[new_row][new_col] == '1' and not visited[new_row][new_col]):
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col))
