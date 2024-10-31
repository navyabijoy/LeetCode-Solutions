class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        count = 0  # Count of zeros in the current window
        l, r = 0, 0  # Left and right pointers
        max_len = 0  # Variable to track the maximum length of the window

        while r < len(nums):  # Traverse through the array with the right pointer
            if nums[r] == 1:  # If the current number is 1
                r += 1  # Expand the window to the right
            else:  # If the current number is 0
                count += 1  # Increment the count of zeros
                r += 1  # Move the right pointer forward

            # Check if we have more zeros than allowed
            while count > k:
                if nums[l] == 0:  # If the leftmost number is 0
                    count -= 1  # Decrement the count of zeros
                l += 1  # Move the left pointer forward

            # Update the max length after adjusting the window
            max_len = max(max_len, r - l)

        return max_len
