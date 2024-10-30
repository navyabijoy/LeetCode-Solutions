class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        res = []
        seen = set()
        for i in range(len(s) - 9): 
            sequence = s[i:i+10]
            if sequence in seen:
                if sequence not in res:
                    res.append(sequence)
            else:
                seen.add(sequence)

        return res




        