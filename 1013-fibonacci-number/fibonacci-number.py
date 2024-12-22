class Solution:
    def fib(self, n: int) -> int:
        a,b=0,1
        if n == 0:
            return a
        elif n==1 or n==2:
            return b
        else:
            return self.fib(n-1) + self.fib(n-2)