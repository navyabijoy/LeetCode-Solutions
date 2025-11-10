class Solution:
    def recurse(self, wordSet, idx, s,dp):
        if idx == len(s):
            return True
        if idx in dp:
            return dp[idx]
        for j in range(idx, len(s)):
            if s[idx:j+1] in wordSet and self.recurse(wordSet,j+1,s,dp):
                dp[idx] = True
                return True
        dp[idx] = False
        return False
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        wordSet = set(wordDict)
        return self.recurse(wordSet, 0, s,dp)


        