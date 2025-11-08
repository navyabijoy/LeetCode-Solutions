class Solution:
    def helper(self, idx, nums, dp):
        if idx < 0:
            return 0
        if idx == 0:
            return nums[0]
        if dp[idx] != -1:
            return dp[idx]
        pick = nums[idx] + self.helper(idx - 2, nums, dp)
        not_pick = self.helper(idx - 1, nums, dp)
        
        dp[idx] = max(pick, not_pick)
        return dp[idx]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n+1)
        ans = self.helper(n-1, nums, dp)
        return ans