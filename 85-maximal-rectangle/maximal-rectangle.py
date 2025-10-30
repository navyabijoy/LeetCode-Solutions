class Solution:
    def largestRectangle(self, arr):
        n = len(arr)
        maxArea = 0
        stack = []
        arr.append(0)
        for i, h in enumerate(arr):
            while stack and arr[stack[-1]] > h:
                height = arr[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        arr.pop()
        return maxArea

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        prefix = [[0] * n for _ in range(m)]
        for j in range(n):
            sum = 0
            for i in range(m):
                sum += int(matrix[i][j])
                if matrix[i][j] == "0":
                    sum = 0
                    prefix[i][j] = 0
                else:
                    prefix[i][j] = sum
        maxArea = 0
        for i in range(m):
            area = self.largestRectangle(prefix[i])
            maxArea = max(maxArea, area)
        return maxArea
