class Solution:
    def isValid(self, s: str) -> bool:
        open_close = { ")": "(", "]": "[", "}" : "{"}
        stack = []
        for ch in s:
            if ch in "[{(":
                stack.append(ch)
            else:
                if stack and open_close[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False