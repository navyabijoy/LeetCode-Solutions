class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        flag = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
                flag = 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if flag == 0:
            return -1
        else:
            return mid