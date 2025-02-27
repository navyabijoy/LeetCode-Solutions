class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int total = 0;
        int left = 0;
        int minSize = Integer.MAX_VALUE;
        for(int right =0; right < nums.length;right++){
            total += nums[right];
            while (total >= target){
                minSize = Math.min(minSize, right-left+1);
                total -= nums[left];
                left++;
            }
            
        }
        return minSize == Integer.MAX_VALUE ? 0 : minSize;

    }
}