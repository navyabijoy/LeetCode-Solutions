class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        countZero = 0
        left = 0
        maxLen = 0
        for right in range(len(nums)):
            
            if nums[right] == 0:
                countZero += 1

            while countZero > k:
                if nums[left] == 0:
                    countZero -= 1
                left += 1
            
            maxLen = max(maxLen, right - left + 1)
        return maxLen