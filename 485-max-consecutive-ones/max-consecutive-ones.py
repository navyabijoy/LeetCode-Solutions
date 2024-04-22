class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, windowSize = 0,0
        for num in nums:
            if num == 1:
                windowSize += 1
            else:
                res = max(res, windowSize)
                windowSize = 0
        res = max(res, windowSize)
        return res
