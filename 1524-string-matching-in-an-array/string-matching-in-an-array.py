class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for word in words:
            for other_word in words:
                if word != other_word and word in other_word:
                    res.append(word)
                    break
        return res
