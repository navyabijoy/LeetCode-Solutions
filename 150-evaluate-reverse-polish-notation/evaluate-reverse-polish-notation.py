class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack_pos = 0  # Keeps track of the "stack" position within tokens
        for i in range(len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                tokens[stack_pos] = int(tokens[i])
                stack_pos += 1
            else:
                # Perform operations using values from tokens (acting as the stack)
                num1 = tokens[stack_pos - 1]
                num2 = tokens[stack_pos - 2]
                
                if tokens[i] == '+':
                    tokens[stack_pos - 2] = num2 + num1
                elif tokens[i] == '-':
                    tokens[stack_pos - 2] = num2 - num1
                elif tokens[i] == '*':
                    tokens[stack_pos - 2] = num2 * num1
                else:
                    tokens[stack_pos - 2] = int(num2 / num1)
                
                # Move stack position down by 1 after performing operation
                stack_pos -= 1
        
        return tokens[0]