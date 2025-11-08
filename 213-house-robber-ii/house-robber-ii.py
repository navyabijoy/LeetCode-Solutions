class Solution:
    def solve(self, idx, nums, dp):
        if idx < 0:
            return 0
        if idx == 0:
            return nums[0]
        if dp[idx] != -1:
            return dp[idx]
        pick = self.solve(idx - 2, nums, dp) + nums[idx]
        not_pick = self.solve(idx - 1, nums, dp)

        dp[idx] = max(pick, not_pick)
        return dp[idx]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp1 = [-1] * (n-1)
        ans1 = self.solve(n - 2, nums[:-1], dp1)

        dp2 = [-1] * (n-1)
        ans2 = self.solve(n - 2, nums[1:], dp2)
        return max(ans1, ans2)
