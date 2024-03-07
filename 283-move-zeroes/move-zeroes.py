class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        slow = 0 #two pointer method, slow one traverses after the fast one
        for fast in range(n): #the fast pointer traverses the array
            if nums[fast]!=0 and nums[slow]==0: #if the value at slow is 0 and the value at fast is non zero
                nums[slow],nums[fast]=nums[fast],nums[slow] #swap the values
               
            
            if nums[slow] != 0: #if the value at slow is non zero, increment slow
                slow +=1
            