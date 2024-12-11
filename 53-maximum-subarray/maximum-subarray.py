class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float('-inf')
        summ = 0
        start = 0
        left, right = -1, -1
        for i in range(len(nums)):
            if summ == 0:
                start = i
            summ += nums[i]
            if(summ > maxi):
                maxi = summ
                left = start
                right = i
            if(summ< 0):
                summ =0
        return maxi


