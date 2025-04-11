class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: # skip finding the seqeunce for the same number
                continue 
            j = i+1
            k = len(nums)-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1 # to check the potential numbers for the same number but different sequence, but since we cant allow duplicates
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        return res
