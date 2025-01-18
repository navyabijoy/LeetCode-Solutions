class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        n = len(nums)
        for i in range(n):
            if nums[i]!=val:
                nums[index]=nums[i]
                index +=1
        return index



               
            

