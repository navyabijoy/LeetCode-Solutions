class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        left = 0
        min_len = float('inf')
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_len = min(right - left + 1, min_len)
                total -= nums[left]
                left += 1
        return min_len if min_len != float('inf') else 0