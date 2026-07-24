class Solution:
    def firstBound(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if left == len(nums) or nums[left] != target:
            return -1
        return left
    
    def lastBound(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target + 1:
                left = mid + 1
            else:
                right = mid
        last = left - 1

        if last < 0 or nums[last] != target:
            return -1

        return last
        

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # res = []
        first = self.firstBound(nums, target)
        last = self.lastBound(nums, target)

        return [first, last]
        