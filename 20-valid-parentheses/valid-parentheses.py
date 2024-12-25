class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        opn = {")":"(","}":"{","]":"["}
        for c in s:
            if c in opn:
                if stack and stack[-1] == opn[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0