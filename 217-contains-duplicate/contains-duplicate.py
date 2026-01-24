class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        track = Counter(nums)
        for num, cnt in track.items():
            if cnt >= 2:
                return True
        return False