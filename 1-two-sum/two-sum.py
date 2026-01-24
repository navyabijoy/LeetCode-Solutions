class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = 0
        index = {}
        for i in range(len(nums)):
            index[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in index and i != index[diff]:
                return [i, index[diff]]


        
