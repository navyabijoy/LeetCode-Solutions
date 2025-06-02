# Last updated: 6/2/2025, 5:45:05 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        n = len(nums)
        for i in range(n):
            if nums[i]!=val:
                nums[index]=nums[i]
                index +=1
        return index



               
            

