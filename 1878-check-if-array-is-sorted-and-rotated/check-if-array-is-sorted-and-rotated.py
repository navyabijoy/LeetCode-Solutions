class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        for i in range(n):
            if(nums[i] < nums[i-1]):
                count += 1
        if(count <= 1):
            return True
        return False