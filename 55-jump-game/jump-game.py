class Solution:
    def canJump(self, nums: List[int]) -> bool:
        peak = 0
        for i in range(len(nums)):
            if i > peak:
                return False
            if nums[i] + i > peak:
                peak = i + nums[i] # peak index or the highest jump you can take from that index
            
            if peak >= len(nums) - 1:
                return True 
        return False


