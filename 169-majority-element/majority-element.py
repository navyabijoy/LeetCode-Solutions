class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxFreq = 0
        seen = {}
        majNum = None
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen[nums[i]] = 0
            seen[nums[i]] += 1
        
        for num,freq in seen.items():
            if maxFreq < freq:
                maxFreq = freq
                majNum = num
        return majNum
            