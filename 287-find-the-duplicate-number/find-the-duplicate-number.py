class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = {}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = True
            else:
                return nums[i]