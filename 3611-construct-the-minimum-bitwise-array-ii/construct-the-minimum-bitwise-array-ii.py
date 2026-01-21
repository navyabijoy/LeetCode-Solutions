class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i, el in enumerate(nums):
            currPosition = 1
            ans = -1
            while (el & currPosition) != 0:  # move until we encounter a `0` bit
                ans = el - currPosition
                currPosition = (
                    currPosition << 1
                )  # keep going left until we encounter a zero
            nums[i] = ans
        return nums
