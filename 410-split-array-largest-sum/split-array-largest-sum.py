class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return -1

        def find_kth(m):
            kth = 1
            summ = 0
            for i in range(len(nums)):
                if summ + nums[i] <= m:
                    summ += nums[i]
                else:
                    kth += 1
                    summ = nums[i]
            return kth

        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = (left + right) // 2
            kth_value = find_kth(mid)
            if kth_value <= k:
                right = mid - 1
            else:
                left = mid + 1

        return left
