class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        new_array = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                new_array.append(matrix[row][col])
        temp = sorted(new_array)
        return temp[k-1]