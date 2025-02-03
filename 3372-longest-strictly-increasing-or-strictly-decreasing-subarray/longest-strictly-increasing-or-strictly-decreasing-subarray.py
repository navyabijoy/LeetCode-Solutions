class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return None
        max_len = inc = dec = 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]: # curr is greater than next
                dec += 1
                inc  = 1
            elif nums[i] < nums[i+1]: # curr is less than next
                inc += 1
                dec = 1
            else: # they are equal
                inc = dec = 1
            max_len = max(max_len,inc,dec)
        return max_len