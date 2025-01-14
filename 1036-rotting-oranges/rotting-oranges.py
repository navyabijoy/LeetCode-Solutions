class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0 # to keep track of time and fresh oranges
        
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: # that means the orange is fresh
                    fresh += 1
                if grid[r][c] == 2: # the rotten orange to the queue
                    q.append([r,c])
        
        # 4 directions to check
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q and fresh > 0: # so while q exists and fresh oranges exists
            for i in range(len(q)):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if(row < 0 or row == len(grid) or col < 0 or col == COLS or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1

        # TC: O(n*m)
        # SC: O(n*m)