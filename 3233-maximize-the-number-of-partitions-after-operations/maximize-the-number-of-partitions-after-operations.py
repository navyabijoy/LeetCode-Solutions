from functools import lru_cache
class Solution:
    @lru_cache(None)
    def solve(self, S, K, i, uniqueChars, canChange):
        if i >= len(S):
            return 0

        charIndex = ord(S[i]) - ord("a")
        newUniqueChar = uniqueChars | (1 << charIndex)
        uniqueCharCount = bin(newUniqueChar).count("1")

        if uniqueCharCount > K:
            res = 1 + self.solve(S, K, i + 1, 1 << charIndex, canChange)
        else:
            res = self.solve(S, K, i + 1, newUniqueChar, canChange)

        if canChange:
            for newCharIndex in range(26):
                newCharSet = uniqueChars | (1 << newCharIndex)
                newUniqueCount = bin(newCharSet).count("1")

                if newUniqueCount > K:
                    res = max(
                        res, 1 + self.solve(S, K, i + 1, 1 << newCharIndex, False)
                    )
                else:
                    res = max(res, self.solve(S, K, i + 1, newCharSet, False))

        return res

    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        return self.solve(s, k, 0, 0, True) + 1
