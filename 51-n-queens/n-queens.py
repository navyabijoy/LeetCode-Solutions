class Solution:
    def solve(self,col,ans,board,n):
        if col == n: # has traversed all the columns
            copy = ["".join(row) for row in board]
            ans.append(copy)
            return

        for row in range(n):
            if(self.isSafe(row,col,ans,board,n)): # if the col, row, and diag is safe to place
                board[row][col] = "Q" # then place the queen
                self.solve(col+1,ans,board,n) # recursively traverse the next column
                # then backtrack
                board[row][col] = "."


    def isSafe(self,row,col,ans,board,n):
        x = row
        y = col

        # check in the same column
        while y>=0:
            if board[x][y] =="Q":
                return False
            y-= 1

        x = row
        y = col

        #check in upper diagonal
        while x >=  0 and y >= 0:
            if board[x][y] == "Q":
                return False
            x -= 1
            y -= 1

        x = row
        y = col
        while x < n and y >= 0:
            if board[x][y] == "Q":
                return False
            y -=1
            x +=1
        return True


    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        ans= []
        self.solve(0,ans, board,n)
        return ans
