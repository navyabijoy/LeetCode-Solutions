class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        while i < n:
            correct = nums[i]
            if correct < n and nums[i] != nums[correct]:
                nums[i],nums[correct] = nums[correct],nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i:
                return i
        return n
      