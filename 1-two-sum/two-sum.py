class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        res = []
        for i in range(len(nums)):
            diff  = target - nums[i]
            if diff in seen:
                res.append(seen[diff])
                res.append(i)

            seen[nums[i]] = i
        return res
