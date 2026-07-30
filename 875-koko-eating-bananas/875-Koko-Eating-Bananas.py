class Solution:
    def isValid(self, piles, hourly, h):
        total = 0
        for i in range(len(piles)):
            total += math.ceil(piles[i] / hourly)
        if total <= h:
            return True
        return False

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right =max(piles)
        ans = 0
        while left <= right:
            mid = (left+right) // 2
            if self.isValid(piles,mid,h):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans