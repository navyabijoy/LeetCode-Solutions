class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            if i & 1:
                bit = ((i + 1) & ~i) >> 1
                ans.append(i & ~bit)
            else:
                ans.append(-1)

        return ans