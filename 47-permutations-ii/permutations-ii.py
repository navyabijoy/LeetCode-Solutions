class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # to deal with duplicates
        res = []

        def backtrack(nums,sol,res,used):
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue # already used it
                elif i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue # avoid duplicated
            
                used[i] = True
                sol.append(nums[i])
                backtrack(nums,sol,res,used)
                sol.pop()
                used[i]= False
                
                
        backtrack(nums,[],res,[False] * len(nums))
        return res