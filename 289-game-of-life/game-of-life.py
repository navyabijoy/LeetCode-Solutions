class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """        
        row = len(board)
        col = len(board[0])
        countLive = 0
        directions = [
        (0, -1), (0, 1),  # Left, Right
        (-1, 0), (1, 0),  # Up, Down
        (-1, -1), (-1, 1),  # Top-Left, Top-Right
        (1, -1), (1, 1)    # Bottom-Left, Bottom-Right
        ]
        for i in range(row):
            for j in range(col):
                if board[i][j] == 1: #live
                    for dr, dc in directions:
                        new_row, new_col = i + dr, j + dc
                        if 0 <= new_row < row and 0 <= new_col < col:

                            if abs(board[new_row][new_col]) == 1:
                                countLive += 1
                    
                    if countLive < 2:
                        board[i][j] = -1
                    elif 2 <= countLive <= 3:
                        board[i][j] = 1
                    elif countLive > 3:
                        board[i][j] = -1
                    countLive = 0

                elif board[i][j] == 0: #dead
                    for dr, dc in directions:
                        new_row, new_col = i + dr, j + dc
                        if 0 <= new_row < row and 0 <= new_col < col:

                            if abs(board[new_row][new_col]) == 1:
                                countLive += 1

                    if countLive == 3:
                        board[i][j] = 2
                    countLive = 0

        for i in range(row):
            for j in range(col):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1                          