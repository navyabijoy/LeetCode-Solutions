class Solution:
    def reverseVowels(self, s: str) -> str:
        words = list(s)
        left = 0
        right = len(s) - 1
        vowel = 'aeiouAEIOU'
        while left < right:
            if words[left] in vowel and words[right] in vowel:
                words[left], words[right] = words[right], words[left]
                left += 1
                right -= 1
            elif words[left] in vowel and words[right] not in vowel:
                right -= 1
            else:
                left += 1
        return "".join(words)
