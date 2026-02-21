class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        left = 0
        track = set()
        for right in range(len(s)):
            while s[right] in track:
                track.remove(s[left])
                left += 1
            
            track.add(s[right])
            maxLen = max(maxLen, right - left + 1)
        return maxLen