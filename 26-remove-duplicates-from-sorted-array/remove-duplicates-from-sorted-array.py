class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if n < 2:
            return n
        left, k = 0,1
        for right in range(1, n):
            if nums[right] != nums[left]:
                left+= 1
                nums[left] = nums[right]
                k+=1
        return k
 