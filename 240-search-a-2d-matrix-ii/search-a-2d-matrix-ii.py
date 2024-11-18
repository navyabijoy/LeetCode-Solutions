class Solution:
    def binary_search(self, arr, n, target):
        left = 0
        right = n - 1
        ans = -1
        while left <= right:
            mid = (left+right) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                right = mid -1 
            else:
                left = mid +1 
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        for r in range(row):
            if self.binary_search(matrix[r], col, target):
                return True
        return False