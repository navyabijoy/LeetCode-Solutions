class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if n < 2:
            return n
        ans, j = 1, 0
        for i in range(1, n):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
                ans += 1
        return ans
 