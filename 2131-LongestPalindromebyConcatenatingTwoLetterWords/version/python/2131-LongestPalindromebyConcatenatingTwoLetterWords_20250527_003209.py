# Last updated: 5/27/2025, 12:32:09 AM
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        hashmap = Counter(words)
        count = 0
        existingPalindrome = 0
        for w, freq in hashmap.items():
            s = w[::-1]
            if w == s:
                count += (freq // 2) * 4
                if freq % 2:
                    existingPalindrome = 1
            elif w < s and s in hashmap:
                count += min(freq, hashmap[s]) * 4
        return count + existingPalindrome * 2