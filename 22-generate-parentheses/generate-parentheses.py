class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n: # there are less open brackets
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop() # backtrack

            if closedN < openN: # if there are less closed brackets compared to open
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()

        backtrack(0,0)
        return res