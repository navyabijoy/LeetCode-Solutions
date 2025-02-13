class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = [[]]
        for n in (nums):
            new_perms = []
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i,n)
                    new_perms.append(p_copy)
            perms = new_perms
        seen = set()
        res = []
        for perm in perms:
            new_p = tuple(perm)
            if new_p not in seen:
                res.append(perm)
                seen.add(new_p)
        return res
        