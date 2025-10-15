class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        k = 0
        prevRun = 0
        currRun = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                currRun += 1
            else: 
                prevRun = currRun
                currRun = 1
            
            k = max(k,currRun // 2)
            k = max(k, min(currRun, prevRun))
            
        return k
            