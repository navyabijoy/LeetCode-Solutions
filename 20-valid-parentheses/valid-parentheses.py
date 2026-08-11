class Solution:
    def isValid(self, s: str) -> bool:
        open_close = { ")":"(","]":"[", "}" : "{"}
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if stack and stack[-1] == open_close[ch]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0