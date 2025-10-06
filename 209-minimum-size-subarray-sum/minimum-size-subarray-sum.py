class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        min_len = float('inf')
        left = 0

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                min_len = min(min_len, right-left+1)
                total -= nums[left]
                left += 1
                
        return 0 if min_len == float('inf') else min_len