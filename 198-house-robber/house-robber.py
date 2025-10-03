class Solution:
    def solve(self,nums,n,dp):
        if n == 0:
            return nums[0]

        if n < 0:
            return  0

        if dp[n] != -1:
            return dp[n]

        incl = self.solve(nums, n-2,dp) + nums[n]
        excl = self.solve(nums,n-1,dp) + 0

        dp[n] = max(incl,excl)
        return dp[n]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n+1)
        ans = self.solve(nums,n-1,dp)
        return ans