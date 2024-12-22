class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num_str = str(x)
        return num_str == num_str[::-1]