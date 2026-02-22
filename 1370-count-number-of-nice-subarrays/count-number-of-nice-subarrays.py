class Solution:
    def atMostK(self, nums,k):
        left = 0
        odd = 0
        count = 0
        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                odd += 1
            while odd > k and left <= right:
                if nums[left] % 2 != 0:
                    odd -= 1
                left += 1
            
            count += right - left + 1
        return count

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k-1)
        