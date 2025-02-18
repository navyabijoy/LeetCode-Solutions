class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        res = []
        seen = set()
        for i in range(len(s)-9):
            sequence = s[i:i+10]
            if sequence in seen: # its being repeated
                if sequence not in res:
                    res.append(sequence) # add the repeated seq in res
            else:
                seen.add(sequence) # encountered first time, add in set
        return res