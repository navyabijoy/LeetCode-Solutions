class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if (m*k) > len(bloomDay):
            return -1
        
        def possible(arr, m, k, day):
            noB, count = 0, 0
            for i in range(len(arr)):
                if arr[i] <= day:
                    count += 1
                else:
                    noB += count // k
                    count = 0
            noB += count // k
            if noB >= m:
                return True
            else:
                return False
        
        left = min(bloomDay)
        right = max(bloomDay)
        ans = right
        while left<= right:
            mid = (left + right) // 2
            if possible(bloomDay, m,k,mid):
                right = mid - 1
            else:
                left = mid + 1
        return left