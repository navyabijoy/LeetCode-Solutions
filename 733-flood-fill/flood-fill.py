class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        q = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        original = image[sr][sc]
        # vis = [[False] * n for _ in range(m)]
        q.append([sr, sc])
        while q:
            r, c = q.popleft()
            if image[r][c] == original:
                image[r][c] = color
            # vis[r][c] = True
            for dr, dc in directions:
                nrow = r + dr
                ncol = c + dc
                if (
                    0 <= nrow < m
                    and 0 <= ncol < n
                    and image[nrow][ncol] != color
                    and image[nrow][ncol] == original
                ):
                    image[nrow][ncol] = color
                    q.append([nrow, ncol])
        return image
