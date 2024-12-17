import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        def find_divisor(arr, thres, num):
            summ = 0
            for i in range(len(arr)):
                summ += math.ceil(arr[i]/num)
            return summ <= thres

        while left <= right:
            mid =(left + right)// 2
            if find_divisor(nums, threshold, mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
