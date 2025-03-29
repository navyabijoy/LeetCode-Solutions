class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        st = set()
        temp = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                hs = set()
                for k in range(j+1, len(nums)):
                    total = nums[i] + nums[j] + nums[k]
                    fourth = target - total
                    if fourth in hs:
                        temp = [nums[i],nums[j],nums[k],fourth]
                        temp.sort()
                        st.add(tuple(temp))
                    hs.add(nums[k])
        ans = [list(t) for t in st]
        return ans


        
        