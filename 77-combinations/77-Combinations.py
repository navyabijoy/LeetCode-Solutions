class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        stack = []

        def backtrack(num):
            if len(stack) == k:
                res.append(stack[:]) # store the copy of the stack
                return

            for i in range(num, n+1):
                stack.append(i)
                backtrack(i+1)
                stack.pop()

        backtrack(1)
        return res