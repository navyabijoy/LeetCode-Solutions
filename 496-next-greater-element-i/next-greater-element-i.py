class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}

        for current in nums2:
            while stack and current > stack[-1]:
                hashmap[stack.pop()] = current
            stack.append(current)
        
        while stack:
            hashmap[stack.pop()] = -1
        ans = []

        for num in nums1:
            ans.append(hashmap[num])
        return ans