class Solution:
    def jump(self, nums: List[int]) -> int:
        peak = 0
        jump_end = 0
        count = 0
        for i in range(len(nums)-1):
            peak = max(peak, nums[i]+i)
            if i == jump_end:
                count += 1
                jump_end = peak
            if jump_end >= len(nums)-1:
                return count
        return count
