class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        rem = {}
        for num in nums:
            r = num % value
            if r not in rem:
                rem[r] = 1
            else:
                rem[r] += 1

        mex = 0
        while (mex % value in rem) and rem[mex % value] > 0:
            rem[mex % value] -= 1
            mex += 1

        return mex
