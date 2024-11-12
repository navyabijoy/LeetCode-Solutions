class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def at_most_k(k):
            if k < 0:
                return 0
            l = 0
            sumx = 0
            count = 0
            for r in range(len(nums)):
                sumx += nums[r]
                while sumx > k:
                    sumx -= nums[l]
                    l += 1
                count += (r - l + 1)
            return count
        
        # The number of subarrays with sum exactly 'goal' is:
        # subarrays with sum at most 'goal' - subarrays with sum at most 'goal - 1'
        return at_most_k(goal) - at_most_k(goal - 1)

        

