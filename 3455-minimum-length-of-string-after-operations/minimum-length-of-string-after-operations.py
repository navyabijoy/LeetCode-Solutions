class Solution:
    def minimumLength(self, s: str) -> int:
        seen = {} # create a hashmap 
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = 0
            seen[s[i]] += 1

        output = 0
        # now we have frequency of each character
        for idx, val in seen.items():
            if val % 2 == 0:
                output += 2
            else:
                output += 1
        return output
