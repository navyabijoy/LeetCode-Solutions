class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        res = [words[0]]
        for i in range(1,n):
            if Counter(res[-1]) != Counter(words[i]): # compare with last added word in res
                res.append(words[i])
        return res