class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Step 1: Remove leading and trailing whitespaces
        if not s:
            return 0  # Return 0 if the string is empty after stripping

        sign = 1  # Step 2: Default sign as positive
        index = 0

        # Step 3: Check for sign in the first character
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1

        res = 0
        while index < len(s) and s[index].isdigit():
            res = res * 10 + int(s[index])  # Accumulate digit by digit
            index += 1

        # Step 4: Apply sign and clamp to 32-bit range
        res *= sign
        res = max(-2**31, min(res, 2**31 - 1))
        
        return res
