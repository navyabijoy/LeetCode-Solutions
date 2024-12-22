class Solution:
    def reverse(self, x: int) -> int:
        summ = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x > 0:
            digit = x % 10
            summ = summ * 10 + digit
            x = x // 10
        
        summ *= sign

        if summ > 2**31 - 1 or summ < - 2**31 - 1:
            return 0

        return summ