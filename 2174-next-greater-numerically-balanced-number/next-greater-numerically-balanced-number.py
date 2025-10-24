class Solution:
    def isBalanced(self,num):
        track = Counter(str(num))
        for ch,n in track.items():
            if int(ch) != n:
                return False
        return True
    def nextBeautifulNumber(self, n: int) -> int:
        num =  n + 1
        while True:
            if self.isBalanced(num):
                return num
            num += 1
