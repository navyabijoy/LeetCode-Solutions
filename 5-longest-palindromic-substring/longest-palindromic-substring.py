class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        resLen = 0
        res = s[0]
        for left in range(len(s)-1):
            for right in range(left+1,len(s)):
                if right-left+1 > resLen and s[left:right+1] == s[left:right+1][::-1]:
                    resLen = right-left+1
                    res = s[left:right+1]
        return "".join(res)


            
            
        