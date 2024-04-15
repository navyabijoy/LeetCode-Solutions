class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        comb = []
        for n in nums2:
            if n in seen:
                comb.append(n)
                seen.remove(n)
        return comb
        #combined = [] #to get the answer in array form
        # for num in nums1:
        #     seen1.add(num)
        # for num in nums2:
        #     seen2.add(num)
            
        # for i in seen1:
        #     for j in seen2:
        #         if i==j:
        #             combined.append(i)
        # return combined
     
