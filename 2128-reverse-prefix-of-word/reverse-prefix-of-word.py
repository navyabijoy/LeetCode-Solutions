class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        pos = word.find(ch)
        prefix = word[0:pos+1]
        new = prefix[::-1]
        res = new + word[pos+1:]
        return res