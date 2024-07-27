class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        n = len(nums)
        leftSum = 0
        for i in range(n):
            rightSum = totalSum - leftSum - nums[i]
            if leftSum == rightSum:
                return i
            else:
                leftSum += nums[i]
        return -1