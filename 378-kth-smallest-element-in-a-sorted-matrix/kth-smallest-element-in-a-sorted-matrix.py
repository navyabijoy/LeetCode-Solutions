class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        minHeap = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                heapq.heappush(minHeap, matrix[i][j])

        for i in range(k-1):
            heapq.heappop(minHeap)
        return minHeap[0]