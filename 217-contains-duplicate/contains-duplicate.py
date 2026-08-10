class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        track = Counter(nums)
        for num, c in track.items():
            if c > 1:
                return True
        return False