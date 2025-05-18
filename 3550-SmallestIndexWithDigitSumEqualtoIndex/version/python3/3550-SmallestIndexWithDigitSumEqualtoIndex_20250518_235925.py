# Last updated: 5/18/2025, 11:59:25 PM
class Solution:
    def digitSum(self,n):
        sum = 0
        while n > 0:
            sum += n % 10  
            n //= 10  
        return sum
        
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if self.digitSum(nums[i]) == i:
                return i
        return -1