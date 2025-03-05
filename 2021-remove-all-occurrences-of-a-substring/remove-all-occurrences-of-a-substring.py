class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        if len(part) > len(s):
            return s

        while part in s:
            find_idx = s.find(part)
            s = s[:find_idx] + s[find_idx + len(part):]
        return s

