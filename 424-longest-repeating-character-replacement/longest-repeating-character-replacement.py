class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s is None:
            return None
        l = 0
        r = 0
        maxans = 0
        max_freq = 0
        string_count = {}
        for r in range(len(s)):
            if s[r] not in string_count:
                string_count[s[r]] = 0
            string_count[s[r]] += 1

            max_freq = max(max_freq, string_count[s[r]])

            if (r - l + 1) - max_freq > k:
                string_count[s[l]] -= 1
                l += 1
                
            maxans = max(maxans, r - l + 1)
        return maxans
