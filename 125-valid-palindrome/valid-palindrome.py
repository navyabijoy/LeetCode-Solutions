class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = []
        for i in range(len(s)):
            if s[i].isalnum():
                newStr.append(s[i].lower())

        left= 0
        right = len(newStr) - 1
        while left <= right:
            if newStr[left] != newStr[right]:
                return False
            left += 1
            right -= 1
        return True