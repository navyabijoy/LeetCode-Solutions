class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        track = Counter(nums)
        for num, freq in track.items():
            if freq == 1:
                return num