class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        l = 0
        r = len(words)-1
        while l <= r:
            words[l],words[r] = words[r], words[l]
            l += 1
            r -= 1
        return " ".join(words)