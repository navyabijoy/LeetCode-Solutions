# Last updated: 6/10/2025, 5:54:11 AM
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        adj_list = {}
        for i, stations in enumerate(routes):
            for station in stations:
                if station not in adj_list:
                    adj_list[station] = []
                adj_list[station].append(i)
        
        queue = deque()
        queue.append([source,0])
        visited_bus = set()

        while queue:
            station, buses_taken = queue.popleft()
            if station == target:
                return buses_taken

            if station in adj_list:
                for bus in adj_list[station]:
                    if bus not in visited_bus:
                        for s in routes[bus]:
                            queue.append([s,buses_taken+1])
                        visited_bus.add(bus)
        return -1