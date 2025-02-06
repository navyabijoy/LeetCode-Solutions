class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                mul = nums[i] * nums[j]
                count += 8 * product_count[mul]
                product_count[mul] += 1
        return count
        
        