class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        dp = [[float('inf')] * m for _ in range(n)]
        minHeap = []
        heapq.heappush(minHeap,(0,0,0))
        moveTime[0][0] = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while minHeap:
            currTime, currRow, currCol = heapq.heappop(minHeap)
            if currTime >= dp[currRow][currCol]:
                continue
            if currRow == n-1 and currCol == m-1:
                return currTime
            
            dp[currRow][currCol] = currTime
            for dr,dc in directions:
                newRow = currRow + dr
                newCol = currCol + dc
                if 0 <= newRow < n and 0 <= newCol < m and dp[newRow][newCol] == float('inf'):
                    nextTime = max(moveTime[newRow][newCol], currTime) + 1
                    heapq.heappush(minHeap, (nextTime, newRow, newCol))
        return -1
