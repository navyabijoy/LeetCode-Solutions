class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        seen = {}
        m = -1
        for i in range(len(nums)):
            sumDigit = 0
            for j in str(nums[i]):
                sumDigit += int(j)
            if sumDigit not in seen:
                seen[sumDigit] = nums[i]
            else:
                m = max(seen[sumDigit] + nums[i], m)
                seen[sumDigit] = max(seen[sumDigit],nums[i])
        return m