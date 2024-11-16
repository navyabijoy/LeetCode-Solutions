class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def get_bit(num, bit):
            temp = (1 << bit)
            temp = temp & num
            if temp == 0:
                return 0
            return 1
        subsets = []
    
        if not nums:
            return [[]]
        else:
            subsets_count = 2 ** len(nums)
            for i in range(0, subsets_count):
                subset = set()
                for j in range(0, len(nums)):
                    if get_bit(i, j) == 1 and nums[j] not in subset:
                        subset.add(nums[j])
                
                if i == 0:
                    subsets.append([])
                else:
                    subsets.append(list(subset))
        return subsets
        