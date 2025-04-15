class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        minCapital = []
        availableProjects=[]

        for i in range(len(capital)):
            heapq.heappush(minCapital, [capital[i],profits[i]]) # creates a min heap

        while k > 0:
            while minCapital and w >= minCapital[0][0]:
                cap, prof = heapq.heappop(minCapital)
                heapq.heappush(availableProjects, -prof)
            
            if not availableProjects:
                break

            w += -heapq.heappop(availableProjects)
            k -= 1
        return w
            

