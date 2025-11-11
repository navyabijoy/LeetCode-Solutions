class Solution:
    def helper(self, pos, dist,m):
        cnt = 1
        last = pos[0]
        for i in range(1, len(pos)):
            if pos[i] - last >= dist:
                cnt += 1
                last = pos[i]
        return cnt >= m
    def maxDistance(self, position: List[int], m: int) -> int:
        low = 1
        position.sort()
        high = (position[-1] - position[0]) // (m - 1)
        while low <= high:
            mid = (low + high) // 2
            if self.helper(position, mid,m):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
        
