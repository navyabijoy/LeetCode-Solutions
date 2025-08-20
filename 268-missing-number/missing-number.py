class Solution:
    def binary_search(self, arr, target):
        left= 0
        right = len(arr) -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        for i in range(n+1):
            if not self.binary_search(nums, i):
                return i
        return n