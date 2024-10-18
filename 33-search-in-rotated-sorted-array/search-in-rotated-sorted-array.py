class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:

            # Finding the mid using floor division
            mid = low + (high - low) // 2

            # Target value is present at the middle of the array
            if nums[mid] == target:
                return mid

            # low to mid is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target and target < nums[mid]:
                    high = mid - 1 # target is within the sorted first half of the array
                else:
                    low = mid + 1 # target is not within the sorted first half, so let’s examine the unsorted second half
            # mid to high is sorted
            else:
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1 # target is within the sorted second half of the array
                else:
                    high = mid - 1 # target is not within the sorted second half, so let’s examine the unsorted first half
        return -1


    
