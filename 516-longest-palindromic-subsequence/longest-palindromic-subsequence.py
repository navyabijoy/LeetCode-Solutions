class Solution:
    def solve(self, text1, text2):
        n = len(text1)
        prev = [0] * (n+1)
        
        
        for i in range(len(text1)):
            curr = [0] * (n+1)
            for j in range(len(text2)):
                ans = 0
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(
                        prev[j],
                        curr[j - 1],
                    )

            prev = curr

        return prev[n - 1]

    def longestPalindromeSubseq(self, s: str) -> int:
        revs = s[::-1]

        return self.solve(s, revs)
