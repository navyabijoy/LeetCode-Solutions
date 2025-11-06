class Solution:
    def dfs(self, i, j, vis, mat):
        m = len(mat)
        n = len(mat[0])
        vis[i][j] = True
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            nrow = i + dr
            ncol = j + dc
            if 0 <= nrow < m and 0 <= ncol < n and not vis[nrow][ncol] and mat[nrow][ncol] == "O":
                self.dfs(nrow, ncol, vis, mat)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        vis = [[False] * n for _ in range(m)]

        for i in range(m):
            if not vis[i][0] and board[i][0] == "O":
                self.dfs(i, 0, vis, board)
            if not vis[i][n - 1] and board[i][n - 1] == "O":
                self.dfs(i, n - 1, vis, board)

        for j in range(n):
            if not vis[0][j] and board[0][j] == "O":
                self.dfs(0, j, vis, board)
            if not vis[m - 1][j] and board[m - 1][j] == "O":
                self.dfs(m - 1, j, vis, board)

        for i in range(m):
            for j in range(n):
                if not vis[i][j] and board[i][j] == "O":
                    board[i][j] = "X"
