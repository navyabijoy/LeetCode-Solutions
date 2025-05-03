class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minHeap = [1]
        seen = {1} # to remove duplicates
        factors = [2,3,5]
        for _ in range(n):
            ugly = heapq.heappop(minHeap) # pop the top most - smallest no.
            for factor in factors:
                new_ugly = ugly * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(minHeap, new_ugly)
        return ugly
        