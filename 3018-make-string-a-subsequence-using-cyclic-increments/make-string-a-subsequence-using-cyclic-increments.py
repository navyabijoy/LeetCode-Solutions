class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        str2Idx, str2Len = 0, len(str2)
        for currChar in str1:
            if str2Idx < str2Len and (ord(str2[str2Idx]) - ord(currChar)) % 26 < 2:
                str2Idx += 1
        return str2Idx == str2Len #since the pointer will only move forward if the target string is present in the given string

            