class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        count = 0
        seen = {'a':0, 'b':0, 'c':0} #hashmap
        for r in range(len(s)):
            if s[r] in seen:
                seen[s[r]] += 1

            while all(value >= 1 for value in seen.values()): # all the alphabets have occured
                count += len(s) - r
                seen[s[l]] -= 1
                l +=1 
        return count
            
