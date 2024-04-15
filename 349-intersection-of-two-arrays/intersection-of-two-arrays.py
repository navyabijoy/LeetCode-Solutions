class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen1 = set()
        seen2 = set()
        combined = [] #to get the answer in array form
        for num in nums1:
            seen1.add(num)
        for num in nums2:
            seen2.add(num)
            
        for i in seen1:
            for j in seen2:
                if i==j:
                    combined.append(i)
        return combined
                