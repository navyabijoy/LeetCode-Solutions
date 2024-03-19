class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_counter = Counter(p) #creates a dictionary for the frequency of every alphabet like { "a": 1, "b": 2 , "c": 1}
        left, right =0, 0 #the two sides of the sliding window
        while right < len(s): #while the string goes on
            p_counter[s[right]] -=1 
            if right-left+1 == len(p):
                if all(val == 0 for val in p_counter.values()):
                    result.append(left)
                p_counter[s[left]] += 1
                left +=1
            right +=1 
        return result


             





        