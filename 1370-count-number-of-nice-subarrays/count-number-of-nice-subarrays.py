class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost_k(k):
            count = 0
            l = 0
            odd_count = 0
            for i in range(len(nums)):
                if nums[i] % 2 == 1:
                    odd_count += 1

                while odd_count > k:
                    if nums[l] % 2 == 1:
                        odd_count -= 1
                    l += 1

                count += (i - l + 1)
            return count
            
        return atmost_k(k) - atmost_k(k-1)


                