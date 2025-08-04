class Solution {
    public boolean containsDuplicate(int[] nums) {
        int n = nums.length;
        HashMap<Integer, Integer> track = new HashMap<>();
        for(int i = 0; i < n; i++){
            if (track.containsKey(nums[i])){
                return true;
            }
            track.put(nums[i], 1);
        }
        return false;
    }
}
