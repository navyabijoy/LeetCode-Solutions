class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        store_string = []
        balance = 0
        for i in range(len(s)):
            if s[i] == '(':
                if balance > 0:
                    store_string.append(s[i])
                balance += 1
            else:
                if balance > 1:
                    store_string.append(s[i])
                balance -= 1


        return "".join(store_string)