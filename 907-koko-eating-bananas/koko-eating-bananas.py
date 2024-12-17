import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        def check_hour(piles, hourly):
            totalH = 0
            n = len(piles)
            for i in range(n):
                totalH += math.ceil(piles[i] / hourly)
            return totalH

        
        while low <= high:
            mid = (low + high) // 2
            totalH = check_hour(piles, mid)
            if totalH <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low
