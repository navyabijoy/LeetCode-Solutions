from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        count_zero = 0
        maxLen = 0
        
        for right in range(len(nums)):
            # Increment count_zero if the current number is 0
            if nums[right] == 0:
                count_zero += 1
            
            # Shrink the window until the number of zeros is <= k
            while count_zero > k:
                if nums[left] == 0:
                    count_zero -= 1
                left += 1
            
            # Update the maximum length
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen
