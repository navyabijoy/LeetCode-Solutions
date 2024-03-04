class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_product = 1
        suff_product = 1
        result = [0]*n

        for i in range(n):
            result[i] = pre_product
            pre_product *= nums[i]
        for i in range(n-1,-1,-1):
            result[i] *= suff_product
            suff_product *= nums[i]
        return result

        