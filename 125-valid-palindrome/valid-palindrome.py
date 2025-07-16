class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for ch in s:
            if ch.isalnum():
                newStr = newStr + ch.lower()
        return newStr == newStr[::-1]