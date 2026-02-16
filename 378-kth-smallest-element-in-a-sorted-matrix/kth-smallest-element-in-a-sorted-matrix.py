class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        r = len(matrix)
        c = len(matrix[0])
        minHeap = []
        for i in range(r):
            for j in range(c):
                heapq.heappush(minHeap, -matrix[i][j])
                while len(minHeap) > k:
                    heapq.heappop(minHeap)
        return -minHeap[0]
                