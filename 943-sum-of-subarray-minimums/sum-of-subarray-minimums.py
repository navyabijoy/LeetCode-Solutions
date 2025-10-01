class Solution:
    def findNse(self, nums):
        stack = []
        nse = [len(nums)] * len(nums)  
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                nse[i] = stack[-1]
            stack.append(i)
        return nse

    def findPse(self, arr):
        stack = []
        pse = [-1] * len(arr)   # default: no PSE → boundary
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                pse[i] = stack[-1]
            stack.append(i)
        return pse

    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        nse = self.findNse(arr)
        pse = self.findPse(arr)
        total = 0
        for i in range(len(arr)):
            left = i - pse[i]       # distance to prev smaller
            right = nse[i] - i      # distance to next smaller
            freq = left * right
            total = (total + arr[i] * freq) % mod
        return total