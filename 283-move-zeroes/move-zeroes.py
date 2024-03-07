class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        slow = 0
        for fast in range(n):
            if nums[fast]!=0 and nums[slow]==0:
                nums[slow],nums[fast]=nums[fast],nums[slow]
               
            
            if nums[slow] != 0:
                slow +=1
            