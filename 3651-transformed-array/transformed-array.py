class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            target_index = ( i + nums[i]) % n
            result[i] = nums[target_index]
        return result