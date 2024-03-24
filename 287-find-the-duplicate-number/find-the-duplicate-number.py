class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen={}
        for s in nums:
            if s in seen:
                return s
            else:
                seen[s] = True



        