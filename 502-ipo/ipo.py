class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profits_heap = [] # max heap
        capital_heap = [] #min heap

        for i in range(0,len(capital)):
            heapq.heappush(capital_heap, (capital[i], i))
        
        
        for _ in range(k):
            while capital_heap and capital_heap[0][0] <= w:
                c,i = heapq.heappop(capital_heap)
                heapq.heappush(profits_heap, (-profits[i], i))

            if not profits_heap:
                break
            
            profit, _ = heappop(profits_heap)
            w += -profit
        return w