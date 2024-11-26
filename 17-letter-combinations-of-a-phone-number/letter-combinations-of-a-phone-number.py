class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keyboard = {
                "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz"
        }
        res = []
        
        def backtrack(index, combination):
            if index == len(digits):
                res.append("".join(combination))
                return
            
            current_digit = digits[index]
            possible_letter = keyboard[current_digit]
            for letter in possible_letter:
                combination.append(letter)
                backtrack(index+1, combination)
                combination.pop()
                
        backtrack(0,[])
        return res
            
