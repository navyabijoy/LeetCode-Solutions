class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        wordLength = len(first_word)
        for s in strs[1:]: #iterate from the second word
            while first_word != s[0:wordLength]:
                wordLength -= 1
                if wordLength == 0:
                    return ""

                first_word = first_word[0:wordLength]
        return first_word



