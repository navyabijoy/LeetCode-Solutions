class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        if nums is None:
            return None

        max_sum = 0
        current_sum = 0
        left = 0
        seen = set()
        for right in range(len(nums)):
            while nums[right] in seen or len(seen) == k:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            
            seen.add(nums[right])
            current_sum += nums[right]

            if len(seen) == k:
                max_sum = max(current_sum, max_sum)
        return max_sum