class Solution:
    def solve(self,arr,index,dp):
        if index >= len(arr):
            return 0
        if dp[index] != -1:
            return dp[index]
        pick = arr[index] + self.solve(arr,index+2,dp)
        notPick = self.solve(arr,index+1,dp)
        dp[index] = max(pick,notPick)
        return dp[index]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        return self.solve(nums,0,dp)