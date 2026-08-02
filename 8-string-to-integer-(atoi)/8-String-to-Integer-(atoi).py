class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  
        if not s:
            return 0  

        sign = 1  
        index = 0

        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1

        res = 0
        while index < len(s) and s[index].isdigit():
            res = res * 10 + int(s[index])  # Accumulate digit by digit
            index += 1

        res *= sign
        res = max(-2**31, min(res, 2**31 - 1))
        
        return res
