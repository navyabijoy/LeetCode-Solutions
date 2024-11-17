class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol =[], []
        n = len(s)
        def isPalindrome(s,start,end):
            while start<=end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
            for c in range(i, n): #to iterate in a specific group of characters
                if isPalindrome(s, i, c):
                    sol.append(s[i:c + 1])
                    backtrack(c+1)
                    sol.pop()
        backtrack(0)
        return res
