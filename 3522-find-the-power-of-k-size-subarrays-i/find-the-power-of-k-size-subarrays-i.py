class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        results = []

        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            unique_sorted = sorted(set(subarray))

            if len(unique_sorted) == k and all(subarray[j] == subarray[0] + j for j in range(k)):
                results.append(max(subarray))
            else:
                results.append(-1)

        return results
        
            