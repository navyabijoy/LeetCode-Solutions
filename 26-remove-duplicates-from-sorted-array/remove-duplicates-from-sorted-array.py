class Solution:
    def removeDuplicates(self, nums):
        
        i = 0
        n = len(nums)
        count = 0
        for j in range(1,n):
            if nums[i] != nums[j]:
                i+=1
                nums[i] = nums[j]
        return i + 1

