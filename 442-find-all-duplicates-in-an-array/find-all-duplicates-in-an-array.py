class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen={}
        duplicates=[]
        for c in nums:
            if c in seen:
                duplicates.append(c)
            else:
                seen[c]= True
        return duplicates

