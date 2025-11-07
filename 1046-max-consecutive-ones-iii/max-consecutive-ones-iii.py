class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count_zero = 0
        left = 0
        maxLen = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count_zero += 1
                
            while nums[right] == 0 and count_zero > k:
                if nums[left] == 0:
                    count_zero -= 1
                left += 1

            if count_zero <= k:
                maxLen = max(maxLen, right - left + 1)
        return maxLen
