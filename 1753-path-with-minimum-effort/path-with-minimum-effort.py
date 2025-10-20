class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        dist = [[float("inf")] * n for _ in range(m)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]  # minimum effort will be at the top

        while heap:
            val, row, col = heapq.heappop(heap)
            if row == m - 1 and col == n - 1:
                return val
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                if 0 <= new_row < m and 0 <= new_col < n:
                    new_val = max(
                        val, abs(heights[new_row][new_col] - heights[row][col])
                    )
                    if new_val < dist[new_row][new_col]:
                        dist[new_row][new_col] = new_val
                        heapq.heappush(heap, (new_val, new_row, new_col))

        return 0