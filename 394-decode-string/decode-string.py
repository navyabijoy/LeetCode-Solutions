class Solution:
    def decodeString(self, s: str) -> str:
        stack= []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[": # while top of the stack is not an opening bracket
                    substr = stack.pop() + substr
                stack.pop() # to pop the opening bracket
                
                # now after the opening bracket, there has to be a number and number can be double digit too
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k # keep popping until the entire number is stored

                stack.append(int(k) * substr)

        return "".join(stack)

                

        