class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        # s1: max sum of an increasing sequence ending at i
        # s2: max sum of inc -> dec sequence ending at i
        # s3: max sum of inc -> dec -> inc sequence ending at i
        s1 = s2 = s3 = float('-inf')
        max_total = float('-inf')

        for i in range(1, n):
            curr = nums[i]
            prev = nums[i-1]
            
            prev_s1, prev_s2, prev_s3 = s1, s2, s3
        
            if curr > prev:
                s1 = max(prev + curr, prev_s1 + curr)
            else:
                s1 = float('-inf')
                
            if curr < prev:
                s2 = max(prev_s1 + curr, prev_s2 + curr)
            else:
                s2 = float('-inf')

            if curr > prev:
                s3 = max(prev_s2 + curr, prev_s3 + curr)
            else:
                s3 = float('-inf')
                
            max_total = max(max_total, s3)

        return max_total