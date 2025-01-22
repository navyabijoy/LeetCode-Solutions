class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        perms = [[]]
        for n in nums:
            new_perms = []
            for p in perms:
                for i in range(len(p)+1): # to insert in every position
                    p_copy = p.copy()
                    p_copy.insert(i,n)
                    new_perms.append(p_copy)
            perms = new_perms
        return perms


