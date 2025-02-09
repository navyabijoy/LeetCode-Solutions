class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        total = n*(n-1)// 2
        seen = defaultdict(int)
        for i in range(n):
            key = nums[i] - i
            count += seen[key]
            seen[key] += 1
        
        return total - count