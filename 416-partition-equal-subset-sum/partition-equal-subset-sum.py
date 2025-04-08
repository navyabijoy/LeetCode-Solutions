class Solution:
    def solve(self,index, nums, target):
        dp = [[False] * (target+1) for _ in range(len(nums)+1)]
        
        for i in range(len(nums)+1):
            dp[i][0] = True
        
        for index in range(len(nums)-1,-1,-1):
            for t in range(1, target+1):
                incl = False
                if(t - nums[index] >= 0):
                    incl = dp[index+1][t - nums[index]]
                excl = dp[index+1][t]
                dp[index][t] = incl or excl

        return dp[0][target]
        
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        N = len(nums)
        
        if total % 2 != 0:
            return False
        
        target = total // 2

        return self.solve(0,nums,target)
