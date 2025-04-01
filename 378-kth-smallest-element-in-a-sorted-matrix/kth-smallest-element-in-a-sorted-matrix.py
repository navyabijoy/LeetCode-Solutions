class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        rows = len(matrix)
        
        minHeap = []
        for r in range(min(rows,k)):
            heappush(minHeap, (matrix[r][0],r,0))

        numbers_checked, smallest_number = 0,0
        while minHeap:
            smallest_number, row_index, col_index = heappop(minHeap)
            numbers_checked += 1
            if numbers_checked == k:
                break
            if col_index + 1 < len(matrix[row_index]):
                heappush(minHeap, (matrix[row_index][col_index+1],row_index, col_index+1))
        return smallest_number
