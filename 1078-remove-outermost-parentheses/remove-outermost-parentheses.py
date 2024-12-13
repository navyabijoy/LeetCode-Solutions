class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        store = []
        balance = 0
        for i in s:
            if i == "(":
                if balance > 0:
                    store.append(i)
                balance +=1
            else:
                if balance > 1:
                    store.append(i)
                balance -=1 
        return "".join(store)
