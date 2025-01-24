from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        for val, freq in count.items():
            if freq > (len(nums)/3):
                res.append(val)
        return res
