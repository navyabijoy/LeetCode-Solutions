class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        ans = -1
        f = self.firstOcc(nums,l,r,ans,target)
        l = self.lastOcc(nums,l,r,ans,target)
        return [f, l]

    def firstOcc(self, nums, l, r, ans, target):
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                ans = m
                r = m - 1
            
            elif nums[m] > target:
                r = m -1
            else:
                l = m + 1
        return ans

    def lastOcc(self, nums, l, r, ans, target):
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                ans = m
                l = m + 1
            
            elif nums[m] > target:
                r = m -1
            else:
                l = m + 1
        return ans