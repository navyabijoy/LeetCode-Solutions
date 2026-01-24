class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            ans = nums[i] + nums[n-i-1]
            res.append(ans)
        return max(res)
