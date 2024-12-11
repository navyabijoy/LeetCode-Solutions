class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for num in nums:
            if num<0:
                neg.append(num)
            else:
                pos.append(num)
        res = []
        for a,b in zip(pos,neg):
            res.append(a)
            res.append(b)
        return res



            