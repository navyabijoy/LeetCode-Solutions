class Solution:
    def solve(self,index, nums, target):
        curr = [False] * (target+1)
        next = [False] * (target+1)

        curr[0] = True
        next[0] = True
        
        for index in range(len(nums)-1,-1,-1):
            for t in range(1, target+1):
                incl = False
                if(t - nums[index] >= 0):
                    incl = next[t - nums[index]]
                excl = next[t]
                curr[t] = incl or excl
            next = curr[:]

        return next[target]
        
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        N = len(nums)
        
        if total % 2 != 0:
            return False
        
        target = total // 2

        return self.solve(0,nums,target)
