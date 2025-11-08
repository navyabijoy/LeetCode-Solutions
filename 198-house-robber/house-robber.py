class Solution:
    def helper(self,nums):
        dp = [0] * (len(nums))

        dp[0] = nums[0]
        for i in range(1, len(nums)):
            pick = nums[i] + dp[i-2]
            not_pick = 0 + dp[i-1]

            dp[i] = max(pick, not_pick)
        return dp[len(nums)-1]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        ans = self.helper(nums)
        return ans
