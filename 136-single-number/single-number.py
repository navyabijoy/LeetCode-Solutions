class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = 0
            seen[nums[i]] += 1
        for num, freq in seen.items():
            if freq == 1:
                return num