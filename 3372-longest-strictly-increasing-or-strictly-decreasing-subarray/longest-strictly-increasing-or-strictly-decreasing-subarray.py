class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return None
        max_len = inc = dec = 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]: # curr is greater than next, so its a decreasing order
                dec += 1 # we increase the decreasing length
                inc  = 1 # and reset the increment length
            elif nums[i] < nums[i+1]: # curr is less than next
                inc += 1 # we increase the indecrement length
                dec = 1 # and reset the decrement length
            else: # they are equal
                inc = dec = 1 # reset both
            max_len = max(max_len,inc,dec) # choose the max number
        return max_len