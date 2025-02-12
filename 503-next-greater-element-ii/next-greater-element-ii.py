class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nge = [-1]*n
        stack = []
        for i in range(2*n):
            while stack and nums[stack[-1]] < nums[i%n]:
                idx = stack.pop()
                nge[idx] = nums[i%n]

            if i < n:
                stack.append(i)
        return nge