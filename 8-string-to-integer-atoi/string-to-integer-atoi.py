class Solution:
    def myAtoi(self, s: str) -> int:
        return self.solve(s.strip())
    def solve(self, s, ans = ''):
        if len(s) > 0 and len(ans) == 0 and s[0] in '+-':
            ans+=s[0]
            return self.solve(s[1:],ans)
        elif len(s)>0 and s[0] in '1234567890':
            ans+= s[0]
            return self.solve(s[1:],ans)
        else: 
            ans = 0 if ans in ['+','-',''] else ans
            ans = int(ans)
            return max(min(ans, 2**31-1),-2**31)
