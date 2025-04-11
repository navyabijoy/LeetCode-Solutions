class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target:
            return 0 # if the start is already greater than target then no need of visiting refueling stops
        i,n = 0, len(stations)
        max_distance = startFuel
        max_heap = []
        stop = 0
        while max_distance < target:
            if i < n and stations[i][0] <= max_distance:
                heapq.heappush(max_heap, -stations[i][1])
                i+=1
            elif not max_heap: # no station is in reachable distance
                return -1
            else:
                max_distance += -heapq.heappop(max_heap)
                stop += 1
        return stop