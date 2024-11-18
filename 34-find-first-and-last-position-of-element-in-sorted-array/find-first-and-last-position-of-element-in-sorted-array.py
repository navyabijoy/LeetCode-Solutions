class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, is_searching_left):
            left = 0
            right = len(nums) - 1
            idx = -1
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    idx = mid
                    if is_searching_left:
                        right = mid-1
                    else:
                        left = mid + 1
            return idx
        
        start_index = binary_search(nums, target, True)
        
        # If the target is not found, no need to search for the rightmost index
        if start_index == -1:
            return [-1, -1]
        
        # Find the rightmost index of the target
        end_index = binary_search(nums, target, False)
        
        return [start_index, end_index]
