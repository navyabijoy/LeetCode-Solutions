class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for point in points:
            x,y = point
            heapq.heappush(minHeap,((x*x+y*y), x, y))
        
        res = []
        while k > 0:
            distance, a, b = heapq.heappop(minHeap)
            res.append([a,b])
            k-= 1
        return res

