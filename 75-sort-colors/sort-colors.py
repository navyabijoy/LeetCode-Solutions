class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1
        curr = 0
        while curr <= right:
            if nums[curr] == 0:
                nums[left],nums[curr] = nums[curr],nums[left]
                left += 1
            elif nums[curr] == 2:
                nums[right],nums[curr]= nums[curr],nums[right]
                right -= 1
                curr-=1
            curr += 1

