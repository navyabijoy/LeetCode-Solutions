class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []
        for i in tokens:
            if i not in ["/","*","+","-"]:
                result.append(int(i))
            else:
            
                num1 = result.pop()
                num2 = result.pop()
                
                if i == '+':
                    result.append(num2 + num1)
                elif i == '-':
                    result.append(num2 - num1)

                elif i == '*':
                    result.append(num2 * num1)

                else:
                    result.append(int(num2 / num1))
                
                
        return result[0]
