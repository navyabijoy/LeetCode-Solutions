class Solution:
    def binarySearch(self,nums,target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr
        if x < arr[0]:
            return arr[:k]
        if x > arr[len(arr)-1]:
            return arr[-k:]

        find_closest = self.binarySearch(arr,x)

        window_left = find_closest-1
        window_right = find_closest
        while (window_right -  window_left - 1) < k:
            if window_left == -1:
                window_right += 1
                continue
            
            if window_right == len(arr) or abs(arr[window_left] - x) <= abs(arr[window_right] - x):
                window_left -= 1
            else:
                window_right += 1
        return arr[window_left+1:window_right]
    