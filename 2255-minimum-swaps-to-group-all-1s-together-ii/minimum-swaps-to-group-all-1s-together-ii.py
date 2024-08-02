class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        N = len(nums)
        total_ones = nums.count(1)
        if total_ones == 0 or total_ones == N:
            return 0
        current_ones = sum(nums[:total_ones])
        max_ones = current_ones

        for i in range(N):
            current_ones -= nums[i]
            current_ones += nums[(i+total_ones) % N]
            max_ones = max(current_ones, max_ones)
        return total_ones - max_ones