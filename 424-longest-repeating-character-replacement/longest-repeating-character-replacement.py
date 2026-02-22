class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxLen = 0
        maxFreq = 0
        freq = {}

        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]] = 1
            else:
                freq[s[right]] += 1
            
            maxFreq = max(maxFreq, freq[s[right]])

            while ((right - left + 1) - maxFreq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1

            maxLen = max(maxLen, right - left + 1)
            
        return maxLen
