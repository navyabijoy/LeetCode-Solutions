class Solution:
    

    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        memo = {}

        def solve(S, K, i, uniqueChars, canChange):
            key = (i << 27) | (uniqueChars << 1) | canChange
            
            if key in memo:
                return memo[key]

            if i >= len(S):
                return 0

            charIndex = ord(S[i]) - ord("a")
            newUniqueChar = uniqueChars | (1 << charIndex)
            uniqueCharCount = bin(newUniqueChar).count("1")

            if uniqueCharCount > K:
                res = 1 + solve(S, K, i + 1, 1 << charIndex, canChange)
            else:
                res = solve(S, K, i + 1, newUniqueChar, canChange)

            if canChange:
                for newCharIndex in range(26):
                    newCharSet = uniqueChars | (1 << newCharIndex)
                    newUniqueCount = bin(newCharSet).count("1")

                    if newUniqueCount > K:
                        res = max(
                            res, 1 + solve(S, K, i + 1, 1 << newCharIndex, False)
                        )
                    else:
                        res = max(res, solve(S, K, i + 1, newCharSet, False))

            memo[key] = res
            return memo[key]
        
        return solve(s, k, 0, 0, True) + 1
