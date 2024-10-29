class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        for i in nums:
            s = i*i
            res.append(s)
        res.sort()
        return res
