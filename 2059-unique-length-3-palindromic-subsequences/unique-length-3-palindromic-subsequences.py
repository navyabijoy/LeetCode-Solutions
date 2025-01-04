class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = set()

        first = {}
        last = {}
        for idx, v in enumerate(s):
            if v not in first:
                first[v] = idx
            last[v] = idx
        #now we have the first and last occurence of the alphabets

        for char in first:
            if first[char] < last[char]: # the alphabet has occured more than once
                middle_char = set(s[first[char]+1:last[char]])

                for m in middle_char:
                    result.add(char+m+char) 
                    # we store the char and the m to avoid removing duplicates in other pairs
        return len(result)