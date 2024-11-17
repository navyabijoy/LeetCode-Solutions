class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        sol = []
        nums =[1,2,3,4,5,6,7,8,9]
        l = len(nums)

        def backtrack(i):
            if i == l:
                if len(sol[:]) == k and sum(sol[:]) == n and sol[:] not in res:
                    res.append(sol[:])
                return
            
            backtrack(i+1)

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

        backtrack(0)
        return res