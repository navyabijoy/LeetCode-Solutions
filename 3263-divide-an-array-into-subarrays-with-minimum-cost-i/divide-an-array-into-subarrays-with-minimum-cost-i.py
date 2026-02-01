class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        total = nums[0]
        min1 = float('inf')
        min2 = float('inf')
        for i in range(1, len(nums)):
            if nums[i] < min1:
                min2 = min1
                min1 = nums[i]
            elif nums[i] <= min2:
                min2 = nums[i]
        total += min1 + min2
        return total


