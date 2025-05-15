class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        return self.backtrack(s,0,seen)
    
    def backtrack(self,s,curr,seen):
        if curr == len(s):
            return 0
        
        max_count = 0
        for i in range(curr+1, len(s)+1):
            substr = s[curr:i]
            if substr not in seen:
                seen.add(substr)
                max_count = max(max_count, 1 + self.backtrack(s,i,seen))
                seen.remove(substr)
        return max_count