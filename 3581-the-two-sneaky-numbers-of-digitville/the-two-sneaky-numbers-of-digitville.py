class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        track = Counter(nums)
        ans = []
        for n, f in track.items():
            if f == 2:
                ans.append(n)
        return ans