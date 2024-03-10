class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if n - 1 not in numSet:  # Only check for the start of a sequence
                current_num = n
                current_streak = 1

                while current_num + 1 in numSet:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest
        
        