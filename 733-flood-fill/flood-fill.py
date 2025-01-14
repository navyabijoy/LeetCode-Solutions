class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])

        initial = image[sr][sc] # this is the initial color 

        if initial == color :
            return image

        q = deque()
        q.append([sr, sc])

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        while q:
            r,c = q.popleft()
            image[r][c] = color

            for dr, dc in directions:
                row, col = r + dr, c + dc
                # Check if the neighbor is valid and has the initial color
                if 0 <= row < ROWS and 0 <= col < COLS and image[row][col] == initial:
                    q.append([row, col])

        return image
