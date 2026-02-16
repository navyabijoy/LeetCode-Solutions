class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        prefix = [[0] * 26 for _ in range(n + 1)]

        for i in range(n): # so, at ith index
            for j in range(26): # which alphabet from the 26, are present
                prefix[i+1][j] = prefix[i][j]
            char_idx = ord(s[i]) - ord('a')
            prefix[i+1][char_idx] += 1
        
        ans = []
        for l, r, k in queries:
            odd = 0
            for j in range(26):
                count = prefix[r + 1][j] - prefix[l][j]
                if count % 2 != 0:
                    odd += 1
        
            if odd // 2 <= k:
                ans.append(True)
            else:
                ans.append(False)
        return ans


