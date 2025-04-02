import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        origin = [0,0]
        for point in points:
            x,y = point
            heapq.heappush(minHeap,(math.dist(point,origin), x, y))
        
        res = []
        while k > 0:
            distance, a, b = heapq.heappop(minHeap)
            res.append([a,b])
            k-= 1
        return res

