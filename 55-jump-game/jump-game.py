class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = 0
        for i, num in enumerate(nums):
            if i > maxIndex:
                return False
            maxIndex = max(maxIndex, num+i)
            if maxIndex >= len(nums) - 1:
                return True
        return False 