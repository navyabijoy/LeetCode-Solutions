class Solution:
    def solve(self,nums,idx,target,dp):

        if idx == len(nums):
            return 1 if target == 0 else 0

        if (idx, target) in dp:
            return dp[(idx,target)]

        add = self.solve(nums, idx + 1, target + nums[idx],dp) 
        sub = self.solve(nums, idx + 1, target - nums[idx],dp) 
        dp[(idx,target)] = add + sub
        return dp[(idx,target)]



    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        ans = self.solve(nums,0,target,dp)
        return ans