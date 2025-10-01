class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        nge = [-1] * n
        
        for i in range(2*n, -1,-1):
            index = i % n # actual index
            
            while stack and nums[i%n] >= stack[-1]:
                stack.pop()

            if i < n:
                nge[i] = stack[-1] if stack else -1
            
            stack.append(nums[index])
        
        return nge