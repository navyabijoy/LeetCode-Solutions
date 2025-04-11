class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0
        max_heap = []
        stops = 0
        i = 0
        n = len(stations)
        max_distance = startFuel
        while max_distance < target:
            if i < n and stations[i][0] <= max_distance:
                heapq.heappush(max_heap, -stations[i][1])
                i += 1
            elif not max_heap: #no stations and we cant reach target
                return -1
            else:
                max_distance += -heapq.heappop(max_heap)
                stops+=1
        return stops

        