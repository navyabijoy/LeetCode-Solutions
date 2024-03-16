class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result =[] #create an array to store the strings
        i=0
        while i <len(word1) or i<len(word2): #since i=0
            if i<len(word1):
                result.append(word1[i])
            if i<len(word2):
                result.append(word2[i])
            i+=1 #i traverses through both the strings and alternatively adds the 'i' character in the string, and i value increases
        return ''.join(result)      
