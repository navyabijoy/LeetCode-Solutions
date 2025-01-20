class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = []
        track = {}
        for i in range(len(nums2)-1,-1,-1):
            while stack:
                if stack[-1] <= nums2[i]:
                    stack.pop()
                else:
                    track[nums2[i]] = stack[-1]
                    stack.append(nums2[i])
                    break

            if not stack:
                track[nums2[i]] = -1
                stack.append(nums2[i])
        
        for j in range(len(nums1)):
            if nums1[j] in track:
                res.append(track[nums1[j]])
        
        return res
