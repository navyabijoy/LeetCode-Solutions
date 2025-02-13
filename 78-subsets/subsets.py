class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i):
            if i == n:
                res.append(sol[:]) # add a copy of sol to res
                return
            
            # dont pick
            backtrack(i+1)
            # pick
            sol.append(nums[i]) # add
            backtrack(i+1) # move to the next number
            sol.pop() # backtrack by pop
        
        backtrack(0)
        return res