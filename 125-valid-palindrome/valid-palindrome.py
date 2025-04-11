class Solution:
    def isPalindrome(self, s: str) -> bool:
        newSentence = ""
        for c in s:
            if c.isalnum(): 
#checks if all the characters in a given string are alphanumeric. Alphanumeric characters include letters (a-z, A-Z) and numbers (0-9).
                newSentence += c.lower()
        return newSentence == newSentence[::-1]