class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        res = []
        trackDuplicates = set()
        for i in range(len(s)-9):
            seqeunce = s[i:i+10]
            if seqeunce in trackDuplicates:
                if seqeunce not in res:
                    res.append(seqeunce)
            else:
                trackDuplicates.add(seqeunce)
        return res