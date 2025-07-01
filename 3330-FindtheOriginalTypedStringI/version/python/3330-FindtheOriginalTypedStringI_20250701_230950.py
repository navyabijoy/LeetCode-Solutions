# Last updated: 7/1/2025, 11:09:50 PM
class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        count = n
        for i in range(1, n):
            if word[i] != word[i-1]:
                count -= 1
        return count

