class Solution:
    def ops(self,num):
        res = ""
        for i in range(1,len(num)):
            res += str((int(num[i-1]) + int(num[i])) % 10)
        return res

    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            s = self.ops(s)

        return s[0] == s[1]