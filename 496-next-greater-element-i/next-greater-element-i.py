class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        track = {}
        stack = []
        maxEle = -1
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            
            if stack:
                track[num] = stack[-1]
            else:
                track[num] = -1
            

            stack.append(num)
        
        final = []

        for m in nums1:
            if m in track:
                final.append(track[m])
        
        return final
            