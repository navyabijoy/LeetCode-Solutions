class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        r=len(nums)-1 
        i=0 #the traversing pointer

        def swap(i,j): #swap function 
            tmp = nums[i]
            nums[i]=nums[j]
            nums[j] = tmp

        while(i<=r): #the traversing ends if i moves ahead if r
            if(nums[i]==0): #if the value is 0
                swap(l,i) #the front pointer and i swap values
                l+=1 #start pointer is incremented
            elif(nums[i]==2): #if the value is 2
                swap(i,r) #the last pointer and i swap value
                r-=1 #r moves a step back
                i-=1 
            i+=1 #i is incremented even if the value is 1
            