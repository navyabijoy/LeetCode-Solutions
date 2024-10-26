class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}
        output= []

        for i in reversed(nums2):
            while stack:
                if stack[-1] > i:
                    hashmap[i] = stack[-1]
                    stack.append(i)
                    break
                else:
                    stack.pop()
            if not stack:
                hashmap[i] = -1
                stack.append(i) 
        for j in nums1:
            output.append(hashmap[j])
        return output

'''
Initialize an empty stack, hashmap and output array.

Iterate through nums2 in reverse.

For each element in nums2, compare the current element with the last element in the stack:
If the last element in the stack > current element, the element on top of the stack is the next greater element. Add this to the hashmap. Also push the current element to the stack as it is candidate for future elements.
If the last element in the stack <= current element, we pop the stack until a greater element is found or the stack is empty.
If the stack is empty, append -1 to the hashmap as there is no greater element. Push the current element to the stack.
After processing nums2, the hashmap will contain each element of nums2 as the key, and its next greater element (or -1) as the value.

Iterate through nums1, retrieve the next greater element from the hashmap for each element, and append it to the output list. This is an O(1) operation.

Return the output.

'''