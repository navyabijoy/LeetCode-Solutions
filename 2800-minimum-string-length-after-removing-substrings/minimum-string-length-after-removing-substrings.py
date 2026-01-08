class Solution:
    def minLength(self, s: str) -> int:
        pair = { "A" : "B", "C" : "D"}
        stack = []
        for ch in s:
            if stack and stack[-1] in pair and ch == pair[stack[-1]]:
                stack.pop()
            else:
                stack.append(ch)
        return len(stack)
         