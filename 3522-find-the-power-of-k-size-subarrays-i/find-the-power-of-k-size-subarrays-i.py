class Solution:
    
        
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        def ifSorted(nums):
            for i in range(len(nums)-1):
                if nums[i+1] != nums[i] + 1:
                    return False
            return True

        n = len(nums)
        results = []

        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            unique_sorted = sorted(set(subarray))

            if len(unique_sorted) == k and ifSorted(subarray):
                results.append(max(subarray))
            else:
                results.append(-1)

        return results

    
            