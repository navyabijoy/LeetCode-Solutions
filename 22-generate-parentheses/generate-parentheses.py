class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(openN, closedN, res):
            if openN == closedN == n:
                ans.append("".join(res))
                return
            
            if openN < n:
                res.append("(")
                backtrack(openN + 1, closedN, res)
                res.pop()
            
            if closedN < openN:
                res.append(")")
                backtrack(openN, closedN + 1, res)
                res.pop()

        backtrack(0,0,[])
        return ans
