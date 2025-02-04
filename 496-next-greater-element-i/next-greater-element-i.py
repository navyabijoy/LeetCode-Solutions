class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        sample = {}
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop() # to get the highest number on the top
            
            if stack:
                sample[num] = stack[-1]
            else:
                sample[num] = -1

            stack.append(num)
        final = []

        for num in nums1:
            if num in sample:
                final.append(sample[num])
        return final
