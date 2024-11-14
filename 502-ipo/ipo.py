class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capitals_min_heap = []
        profits_max_heap = []
        
        # Insert all capital values with their indices into the min heap
        for x in range(0, len(capital)):
            heappush(capitals_min_heap, (capital[x], x))
        
        for _ in range(k):
            # Move all projects that can be started with current capital to the max-heap of profits
            while capitals_min_heap and capitals_min_heap[0][0] <= w:
                c, i = heappop(capitals_min_heap)
                heappush(profits_max_heap, (-profits[i], i))  # Push negative profit to simulate max-heap
            
            if not profits_max_heap:
                break

            # Select the project with the maximum profit
            profit, _ = heappop(profits_max_heap)
            w += -profit  # Add the profit to current capital (negating it to positive)

        return w
