class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r,c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or #r and c are less than 0
                r >= ROWS or c >= COLS or #r and c are out of board
                word[i] != board[r][c] or #if 
                (r,c) in path): #if character is already in set
                return False
            
            path.add((r,c))
            res = (dfs(r + 1, c, i + 1)or
                    dfs(r - 1, c, i + 1) or
                    dfs(r, c + 1, i + 1) or
                    dfs(r, c - 1, i + 1))
            path.remove((r,c))
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False