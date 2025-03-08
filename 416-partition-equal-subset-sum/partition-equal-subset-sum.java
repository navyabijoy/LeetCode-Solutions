class Solution {
    private boolean helper(int idx, int[] arr, int n, int target, Boolean[][] dp){
        // base cases
        if(idx >= n){
            return false;
        }
        if(target<0){
            return false;
        }
        if(target==0){
            return true;
        }
        if(dp[idx][target] != null){ // step 3
            return dp[idx][target]; 
        }

        boolean pick = helper(idx + 1, arr, n, target - arr[idx],dp);
        boolean notPick = helper(idx + 1, arr, n, target,dp);

        return dp[idx][target] = pick || notPick; // step 2
    }
    public boolean canPartition(int[] nums) {
        int N = nums.length;
        int total = 0;
        for(int i = 0;i<N;i++){
            total = total + nums[i];
        }
        if(total % 2 !=0){
            return false;
        }
        int target = total / 2;
        Boolean[][] dp = new Boolean[N][target+1]; // step 1
        return helper(0, nums, N, target,dp);
    }
}