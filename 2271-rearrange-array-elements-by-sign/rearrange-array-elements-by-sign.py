class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
            
        new = []

        for i in range(len(nums)//2):
            new.append(pos[i])
            new.append(neg[i])
        
        return new