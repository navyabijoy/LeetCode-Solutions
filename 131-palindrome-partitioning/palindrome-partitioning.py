class Solution:
    def isPali(self,s,left,right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def backtrack(i, res):
            if i == len(s):
                ans.append(res[:])
                return
            
            for j in range(i, len(s)):
                if self.isPali(s,i,j):
                    res.append(s[i:j+1])
                    backtrack(j+1,res)
                    res.pop()
        backtrack(0,[])
        return ans