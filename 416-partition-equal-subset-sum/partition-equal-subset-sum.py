class Solution:
    def solve(self, nums, target):
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n) ]

        for i in range(n):
            dp[i][0] = True

        if nums[0] <= target:
            dp[0][nums[0]] = True
        
        for i in range(1,n):
            for t in range(1, target+1):
                incl = False
                if nums[i] < t:
                    incl = dp[i- 1][t - nums[i]]
                excl = dp[i - 1][t - 0]
                dp[i][t] = incl or excl

        return dp[n-1][target]

    def canPartition(self, nums: List[int]) -> bool:
        if (sum(nums) % 2 != 0):
            return False
        n = len(nums)
        target = sum(nums) // 2
        
        return self.solve(nums, target)