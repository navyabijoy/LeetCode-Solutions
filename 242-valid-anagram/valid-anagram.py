class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = {}
        t_count = {}

        for i in range(len(s)):
            if s[i] in s_count:
                s_count[s[i]] += 1
            else:
                s_count[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in t_count:
                t_count[t[i]] += 1
            else:
                t_count[t[i]] = 1
        
        return s_count == t_count