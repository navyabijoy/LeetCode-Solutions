class Solution {
    public boolean check(int[] nums) {
        int count = 0;
        int n = nums.length;
        for(int i=0;i<n;i++){
            if(nums[(i-1+n)%n] > nums[i]){
                count++;
            }
        }
        return count<=1;
    }
}