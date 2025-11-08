class Solution:
    def helper(self,nums):
        # dp = [0] * (len(nums))
        if len(nums) == 1:
            return nums[0]
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            pick = nums[i] + prev2
            not_pick = 0 + prev1
            curr = max(pick, not_pick)
            prev2 = prev1
            prev1 = curr
        return prev1

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        ans = self.helper(nums)
        return ans
