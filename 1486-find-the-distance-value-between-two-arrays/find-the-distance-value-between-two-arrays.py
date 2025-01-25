class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr1.sort()
        arr2.sort()
        total = 0
        for i in range(len(arr1)):
            idx = self.binary_search(arr2, arr1[i])
            valid = True
            if idx < len(arr2) and abs(arr2[idx] - arr1[i]) <= d:
                valid = False
            if idx > 0 and abs(arr2[idx-1] - arr1[i]) <= d:
                valid = False
            if valid:
                total += 1
        return total

    def binary_search(self,nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
        