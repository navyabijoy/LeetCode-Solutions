class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        count = Counter(nums)
        for num, c in count.items():
            if c == n:
                return num