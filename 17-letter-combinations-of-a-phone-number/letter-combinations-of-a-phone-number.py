class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keyboard = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs",'8':"tuv","9":"wxyz"}
        res = [""] 
        for digit in digits:
            comb = keyboard[digit]
            substr = []
            for prefix in res:
                for letter in comb:
                    substr.append(prefix + letter)
            res = substr
        return res
            
