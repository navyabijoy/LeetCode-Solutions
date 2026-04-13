class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        ptr1 = 0
        ptr2 = 0
        while word1 and word2 and ptr1 < len(word1) and ptr2 < len(word2):
            res.append(word1[ptr1])
            res.append(word2[ptr2])
            ptr1 += 1
            ptr2 += 1
        
        res.append(word1[ptr1:])
        res.append(word2[ptr2:])
        
        return "".join(res)