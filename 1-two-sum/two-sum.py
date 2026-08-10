class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and i != nums.index(diff):
                result = [i, nums.index(diff)]
        return result