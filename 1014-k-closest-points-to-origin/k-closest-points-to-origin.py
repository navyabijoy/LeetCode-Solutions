class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        res = []

        for point in points:
            x,y = point
            distance = -(x*x+y*y)
            heapq.heappush(maxHeap,(distance, x, y))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return [[x,y] for dist, x, y in maxHeap]

