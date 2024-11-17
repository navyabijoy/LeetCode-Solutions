class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        nums.sort()
        n = len(nums)

        def backtrack(i):
            if i == n:
                if sol[:] not in res:
                    res.append(sol[:])
                return
            
            backtrack(i+1)

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return res