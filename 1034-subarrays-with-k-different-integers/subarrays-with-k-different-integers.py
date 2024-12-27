class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmostK(nums,k):
            count = 0
            left = 0
            seen = {}
            for right in range(len(nums)):
                if nums[right] in seen:
                    seen[nums[right]] += 1
                else:
                    seen[nums[right]] = 1
                while len(seen) > k:
                    seen[nums[left]] -= 1
                    if seen[nums[left]] == 0:
                        del seen[nums[left]]
                    left += 1

                count += right - left + 1
            return count

        return atmostK(nums, k) - atmostK(nums,k-1)