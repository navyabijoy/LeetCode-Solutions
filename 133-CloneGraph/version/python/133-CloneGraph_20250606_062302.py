# Last updated: 6/6/2025, 6:23:02 AM
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        minHeap = []
        minTime = {}
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        
        heapq.heappush(minHeap,(0,k)) # (distance from source, source)
        while minHeap:
            time_k_to_i, i = heapq.heappop(minHeap)

            if i in minTime:
                continue
            minTime[i] = time_k_to_i
            for nei in graph[i]:
                nei_node,nei_time = nei
                if nei_node not in minTime:
                    heapq.heappush(minHeap, (time_k_to_i + nei_time, nei_node))
                    
        if len(minTime) == n:
            return max(minTime.values())
        else:
            return -1 

        