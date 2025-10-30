class Solution:
    def NextSmaller(self,arr):
        stack = []
        n = len(arr)
        nse = [n] * n
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            nse[i] = stack[-1] if stack else n
            stack.append(i)
        return nse
    
    def PrevSmaller(self,arr):
        stack = []
        n = len(arr)
        pse = [-1] * n
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            pse[i] = stack[-1] if stack else -1
            stack.append(i)
        return pse

    def largestRectangleArea(self, heights: List[int]) -> int:
        nse = self.NextSmaller(heights)
        pse = self.PrevSmaller(heights)
        maxArea = float('-inf')
        for i in range(len(heights)):
            area = heights[i] * (nse[i] - pse[i] - 1)
            maxArea = max(maxArea, area)
        return maxArea