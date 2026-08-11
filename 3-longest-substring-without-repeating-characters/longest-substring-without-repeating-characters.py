class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        track = set()
        left = 0
        for right in range(len(s)):
            while s[right] in track:
                track.remove(s[left])
                left += 1
            track.add(s[right])
            maxLen = max(right - left + 1, maxLen)
        return maxLen
