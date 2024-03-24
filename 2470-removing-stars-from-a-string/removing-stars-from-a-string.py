class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for c in s:
            if c == '*':
                if stack and stack[-1] != "*":
                    stack.pop()
            else:
                stack.append(c) 
        return ''.join(stack)
        
        