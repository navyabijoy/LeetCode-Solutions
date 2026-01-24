class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        strack = Counter(s)
        ttrack = Counter(t)
        return strack == ttrack