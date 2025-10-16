class Solution:
    def solve(self,arr,curr_sum,target,i,dp):
        if i == len(arr) and target == curr_sum:
            return 1

        if i == len(arr):
            return 0
        
        if (curr_sum,i) in dp:
            return dp[(curr_sum,i)]
        
        incl = self.solve(arr,curr_sum + arr[i], target,i+1,dp)
        excle =self.solve(arr,curr_sum - arr[i],target,i+1,dp)

        dp[(curr_sum,i)] = incl + excle
        return dp[(curr_sum,i)]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp ={}
        ans = self.solve(nums,0,target,0,dp)
        return ans