class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        count = 0
        preSum = 0
        # O(N x log N) we have taken a simple map so log N, if 
        for i in range(len(nums)):
            preSum += nums[i]
            remove = preSum - k
            if remove in hashmap:
                count += hashmap[remove]
            if preSum not in hashmap:
                hashmap[preSum] = 0
            hashmap[preSum] += 1
        return count