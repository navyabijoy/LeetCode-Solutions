class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]: #if the string dont meet at pointer l and r
                skipL, skipR = s[l+1:r+1], s[l:r] 
                #skipL means, we are incrementing left by 1, now if we just write 
                #[l+1:r] python doesnt detect 'r' but takes it at 'r-1'
                #now in skip r, we are decrementing 'r' so that it moves the pointer
                #forward, now [l:r] is already considered [l:r-1]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            l +=1
            r-=1
        return True