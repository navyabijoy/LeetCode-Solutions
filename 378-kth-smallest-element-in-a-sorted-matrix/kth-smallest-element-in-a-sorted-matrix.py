class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minheap = []
        m = len(matrix)
        # since the arrays are sorted, add the first index to heap
        for i in range(m):
            heapq.heappush(minheap, (matrix[i][0], i, 0))  # val, row, col

        maxheap = []
        while minheap:
            val, row, col = heapq.heappop(minheap)

            heapq.heappush(maxheap, -val)

            while len(maxheap) > k:
                heapq.heappop(maxheap)

            if col + 1 < len(matrix[row]):
                heapq.heappush(minheap, (matrix[row][col + 1], row, col + 1))

        return -maxheap[0]
