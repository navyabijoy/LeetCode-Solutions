class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxOnes = float('-inf')
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            maxOnes = max(maxOnes, count)
        return maxOnes