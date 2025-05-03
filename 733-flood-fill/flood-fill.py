class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        temp = image[sr][sc]
        if temp == color:
            return image

        def backtrack(r,c):
            if r >= m or c >= n or r < 0 or c < 0:
                return

            if image[r][c] != temp:
                return
            
            image[r][c] = color

            direction = [[0,1],[0,-1],[1,0],[-1,0]]
            for track in direction:
                newRow = r + track[0]
                newCol = c + track[1]
                 # the cell should be the same as the org color
                backtrack(newRow,newCol)

        backtrack(sr,sc)
        return image
