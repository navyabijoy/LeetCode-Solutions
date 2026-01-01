class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for d in digits:
            num += str(d)
        sum = int(num) + 1
        res = []
        for s in str(sum):
            res.append(int(s))
        return res