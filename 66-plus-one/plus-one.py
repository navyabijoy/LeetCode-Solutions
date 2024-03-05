class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1,-1,-1): #iterates through the list in reverse order
            if digits[i] == 9: #if the digit encountered is 9, then replaces 9 with 0
                digits[i]=0 #9 is replaced with 0
            else:
                digits[i] = digits[i] + 1 #if the digit is a non 9 number then 1 is added
                return digits #and returns the array as only 1 number is supposed to be incremented
     
        return [1] + digits #this statement happens when the array encountered is an all 9 array, and the resultant array left is [0,0,0] after being replaced by 0, 1 is supposed 
        #to be added, '+' is used to concatenate the two arrays


            

            

        
