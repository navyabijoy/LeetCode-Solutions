class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        new = []
        i = 0
        j = 0
        while i < l1 and j < l2:
            new.append(word1[i])
            i += 1
            new.append(word2[j])
            j += 1
        new.append(word1[i:])
        new.append(word2[j:])
        return "".join(new)
