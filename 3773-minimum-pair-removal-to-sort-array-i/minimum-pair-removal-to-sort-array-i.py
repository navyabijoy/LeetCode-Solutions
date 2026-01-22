class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0

        def is_sorted(arr):
            return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
        
        while not is_sorted(nums):
            min_sum = float('inf')
            idx = 0

            for i in range(len(nums)-1):
                s = nums[i] + nums[i+1]
                if s < min_sum:
                    min_sum = s
                    idx = i
            
            nums = nums[:idx] + [min_sum] + nums[idx+2:]
            ops += 1
        
        return ops