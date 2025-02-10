class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack and s[i] in '0123456789':
                stack.pop()
                # stack.pop()
            else:
                stack.append(s[i])

        return "".join(stack)
            
