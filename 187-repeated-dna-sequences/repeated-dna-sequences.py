class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        res = []
        final = set()
        for i in range(len(s)-9):
            seq = s[i:i+10]
            if seq in final:
                if seq not in res:
                    res.append(seq)
            else:
                final.add(seq)
        return res