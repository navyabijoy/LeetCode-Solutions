class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        left = 0
        max_sum = 0
        curr_sum = 0
        seen = set() # to have distinct numbers
        for right in range(len(nums)):
            while nums[right] in seen or len(seen) == k:
                seen.remove(nums[left])
                curr_sum -= nums[left]
                left += 1

            seen.add(nums[right])
            curr_sum += nums[right]
            if len(seen)== k:
                max_sum = max(max_sum, curr_sum)
        return max_sum