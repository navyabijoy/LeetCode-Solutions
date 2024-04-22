class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res=[]
        for x in nums:
            if len(str(x)) %2 == 0:
                res.append(x)
        return len(res)
        
        
        #return len([x for x in nums if len(str(x))%2==0])  
        