class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_product = 1 #used 2 arrays, one to solve the product of numbers from the beginning 
        suff_product = 1 #one to store the product of numbers from the last 
        result = [0]*n #store the final result

        for i in range(n):
            result[i] = pre_product #iterates through the first array
            pre_product *= nums[i] #number multiplies itself with the number before it e.g. [2,4,6,3] = [2,8,48,144]
        for i in range(n-1,-1,-1): #reverse iterations
            result[i] *= suff_product
            suff_product *= nums[i] #[2,4,6,3] = [144,72,18,3]
        return result

        
