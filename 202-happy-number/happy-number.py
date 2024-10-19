class Solution:
    def isHappy(self, n: int) -> bool:

        def SumOfSquare(num):
            output = 0
            while num:
                digit = num % 10  # Access the last digit
                output += digit ** 2  # Square the digit and add it to the output
                num = num // 10  # Get the remaining digits
            return output

        slow = n
        fast = SumOfSquare(n)

        # We use slow and fast pointers to detect a cycle
        while fast != 1 and slow != fast:
            slow = SumOfSquare(slow)  # Move slow one step
            fast = SumOfSquare(SumOfSquare(fast))  # Move fast two steps

        return fast == 1  # If fast reaches 1, the number is happy
