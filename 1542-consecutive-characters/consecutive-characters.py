class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return
        
        res, count = 1, 1
        for char in range(1, len(s)):
            if s[char] == s[char-1]:
                count +=1
                res = max(res,count)

            else:
                count=1
        return res