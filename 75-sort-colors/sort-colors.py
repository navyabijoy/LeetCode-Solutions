class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr = 0
        start = 0
        end = len(nums)-1
        while curr <= end:
            if nums[curr]==0:
                nums[curr], nums[start] = nums[start], nums[curr]
                curr += 1
                start +=1
            elif nums[curr] == 1:
                curr += 1
            else:
                nums[end], nums[curr] = nums[curr], nums[end]
                end -= 1
        return nums