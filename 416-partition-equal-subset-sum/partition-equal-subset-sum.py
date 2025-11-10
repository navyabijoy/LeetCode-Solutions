class Solution:
    def solve(self, idx, nums, target, dp):
        if idx < 0:
            return False
        if idx == 0:
            return nums[idx] == target
        if target < 0:
            return False
        if target == 0:
            return True
        if dp[idx][target] != -1:
            return dp[idx][target]
        incl = self.solve(idx - 1, nums, target - nums[idx], dp)
        excl = self.solve(idx - 1, nums, target - 0, dp)
        dp[idx][target] = incl or excl
        return dp[idx][target]

    def canPartition(self, nums: List[int]) -> bool:
        if (sum(nums) % 2 != 0):
            return False
        n = len(nums)
        target = sum(nums) // 2
        dp = [ [-1] * (target + 1) for _ in range(n) ]
        return self.solve(n-1, nums, target,dp)