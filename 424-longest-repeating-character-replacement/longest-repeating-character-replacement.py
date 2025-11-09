class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxFreq = 0
        maxLen = 0
        freq = [0] * 26
        for right in range(len(s)):
            freq[ord(s[right]) - ord('A')] += 1
            maxFreq = max(maxFreq, freq[ord(s[right]) - ord('A')])

            while (right - left + 1) - maxFreq > k: 
                # meaning, another character is becoming more freq 
                freq[ord(s[left]) - ord('A')] -= 1
                # maxFreq = 0
                # for i in range(26):
                #     maxFreq = max(maxFreq, freq[i])
                left += 1
            
            # if (right - left + 1) <= k:
            maxLen = max(maxLen, right - left + 1)
        return maxLen