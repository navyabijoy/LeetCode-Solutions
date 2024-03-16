class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        seen = {}  # HashMap to store characters of s

        # Populate seen with characters of s
        for char in s:
            seen[char] = True

        # Check if characters in t match with characters in seen
        s_pointer = 0
        for char in t:
            if s_pointer == len(s):
                break
            if char == s[s_pointer]:
                s_pointer += 1
        return s_pointer == len(s)
        