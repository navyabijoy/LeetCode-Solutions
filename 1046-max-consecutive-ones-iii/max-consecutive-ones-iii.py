class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero = 0
        left = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero += 1
            
            while zero > k:
                if nums[left] == 0:
                    zero -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
        return max_len
            

            