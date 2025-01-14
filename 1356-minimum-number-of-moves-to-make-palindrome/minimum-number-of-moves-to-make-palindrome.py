class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)

        moves = 0
        i,j = 0, len(s)-1
        while i < j:
            k = j
            while k > i:
                if s[i] == s[k]:
                    for m in range(k,j):
                        s[m], s[m+1] = s[m+1] , s[m]
                        moves += 1
                    j -= 1
                    break
                k -= 1
            
            if  k == i:
                moves += len(s) // 2 -i
            i+= 1
        return moves