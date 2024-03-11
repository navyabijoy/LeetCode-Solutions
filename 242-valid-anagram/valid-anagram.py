class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ascii = [ord(char)for char in s]
        t_ascii=[ord(char)for char in t]
        s_ascii.sort()
        t_ascii.sort()
        if s_ascii == t_ascii:
            return True
        else:
            return False