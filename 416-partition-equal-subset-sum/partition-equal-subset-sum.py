class Solution:
    def helper(self, idx, arr, n, target,dp):
        # base cases
        if idx >= n:
            return False

        if target < 0:
            return False
        
        if target == 0:
            return True

        if dp[idx][target] != -1: # step 3
            return dp[idx][target]

        pick = self.helper(idx+1, arr, n, target - arr[idx],dp)
        notPick = self.helper(idx+1, arr, n, target - 0,dp)
        dp[idx][target] =  pick or notPick # step 2
        return dp[idx][target]

    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        total = sum(nums)

        if total % 2 != 0: #its odd
            return False # array cant be split

        target = total // 2
        dp = [[-1] * (target + 1) for _ in range(N)]  # step 1
        return self.helper(0,nums,N,target,dp)
    