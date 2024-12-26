class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        hashmap = {}
        stack = []
        for i in range(len(nums2)-1,-1,-1):
            while stack:
                if stack[-1] <= nums2[i]:
                    stack.pop()
                else:
                    hashmap[nums2[i]] = stack[-1]
                    stack.append(nums2[i])
                    break
            if not stack:
                hashmap[nums2[i]] = -1
                stack.append(nums2[i])
        for j in nums1:
            if j in hashmap:
                output.append(hashmap[j])
        return output



            
            

            
