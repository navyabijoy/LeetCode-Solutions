class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def helper(s):
            if len(s) == 0:
                return True

            if s in memo:
                return memo[s]

            for word in wordDict:
                #traversing through each word in dictionary
                if s.startswith(word):
                    if helper(s[len(word):]):
                        memo[s] = True
                        return True
            memo[s] = False
            return False
        
        return helper(s)
