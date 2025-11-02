class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        track = [['0'] * n for _ in range(m)]

        for i,j in guards:
            track[i][j] = 'G'
        for i,j in walls:
            track[i][j] = 'W'

        directions = [ (0,1), (1,0), (0,-1), (-1,0)]

        for i, j in guards:
            for dr, dc in directions:
                newr = dr + i
                newc = dc + j
                while 0 <= newr < m and 0 <= newc < n and track[newr][newc] not in ('W','G'):
                    if track[newr][newc] == '0':
                        track[newr][newc] = 'V'
                    # move one more step in that same direction
                    newr += dr
                    newc += dc
        
        
        count = 0
        for i in range(m):
            for j in range(n):
                if track[i][j] == '0':
                    count += 1
        return count
                