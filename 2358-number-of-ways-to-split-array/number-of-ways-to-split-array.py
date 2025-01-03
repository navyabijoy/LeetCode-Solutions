class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        curr_sum = total_sum
        count = 0

        for i in range(len(nums)-1):
            curr_sum -= nums[i]
            if curr_sum <= (total_sum - curr_sum):
                count += 1
        return count