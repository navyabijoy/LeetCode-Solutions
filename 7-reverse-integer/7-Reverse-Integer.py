class Solution:
    def reverse(self, x: int) -> int:
        summ = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x > 0:
            digit = x % 10 # returns the last gift hence a reversed number
            summ = summ * 10 + digit
            x = x // 10
        
        summ *= sign # gives the number the -ve or +ve sign

        if summ > 2**31 - 1 or summ < - 2**31 - 1: #the result should be in the int range
            return 0

        return summ